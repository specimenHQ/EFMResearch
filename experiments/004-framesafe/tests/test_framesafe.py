import socket
import struct
import sys
import threading
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from framesafe import (
    FrameTimeout, OversizedFrame, TruncatedFrame,
    echo_connection, encode_frame, recv_frame, send_frame
)


class FrameSafeTests(unittest.TestCase):
    def socketpair(self):
        return socket.socketpair()

    def test_fragmented_header_and_payload(self):
        a, b = self.socketpair()
        try:
            raw = encode_frame(b"hello")
            def sender():
                for byte in raw:
                    a.sendall(bytes([byte]))
                    time.sleep(0.001)
            t = threading.Thread(target=sender); t.start()
            self.assertEqual(recv_frame(b, timeout=1), b"hello")
            t.join()
        finally:
            a.close(); b.close()

    def test_adjacent_empty_and_binary_frames(self):
        a, b = self.socketpair()
        try:
            a.sendall(encode_frame(b"") + encode_frame(b"\x00\xff") + encode_frame(b"x"))
            self.assertEqual(recv_frame(b), b"")
            self.assertEqual(recv_frame(b), b"\x00\xff")
            self.assertEqual(recv_frame(b), b"x")
        finally:
            a.close(); b.close()

    def test_clean_eof_before_header(self):
        a, b = self.socketpair()
        a.close()
        try:
            self.assertIsNone(recv_frame(b))
        finally:
            b.close()

    def test_partial_header_is_error(self):
        a, b = self.socketpair()
        try:
            a.sendall(b"\x00\x00")
            a.shutdown(socket.SHUT_WR)
            with self.assertRaises(TruncatedFrame):
                recv_frame(b)
        finally:
            a.close(); b.close()

    def test_partial_payload_is_error(self):
        a, b = self.socketpair()
        try:
            a.sendall(struct.pack("!I", 5) + b"ab")
            a.shutdown(socket.SHUT_WR)
            with self.assertRaises(TruncatedFrame):
                recv_frame(b)
        finally:
            a.close(); b.close()

    def test_exact_max_and_max_plus_one(self):
        a, b = self.socketpair()
        try:
            send_frame(a, b"12345678", max_frame=8)
            self.assertEqual(recv_frame(b, max_frame=8), b"12345678")
            with self.assertRaises(OversizedFrame):
                encode_frame(b"123456789", max_frame=8)
        finally:
            a.close(); b.close()

    def test_oversized_header_rejected_without_payload(self):
        a, b = self.socketpair()
        try:
            a.sendall(struct.pack("!I", 9))
            with self.assertRaises(OversizedFrame):
                recv_frame(b, max_frame=8)
        finally:
            a.close(); b.close()

    def test_total_deadline_defeats_slow_trickle(self):
        a, b = self.socketpair()
        try:
            raw = encode_frame(b"abcd")
            def slow_sender():
                try:
                    for byte in raw:
                        time.sleep(0.04)
                        a.sendall(bytes([byte]))
                except OSError:
                    pass
            t = threading.Thread(target=slow_sender); t.start()
            start = time.monotonic()
            with self.assertRaises(FrameTimeout):
                recv_frame(b, timeout=0.12)
            self.assertLess(time.monotonic() - start, 0.22)
            a.close()
            t.join()
        finally:
            try: a.close()
            except OSError: pass
            b.close()

    def test_echo_connection_multiple_frames(self):
        a, b = self.socketpair()
        result = {}
        try:
            def server():
                result["count"] = echo_connection(b, max_frame=100, timeout=1)
            t = threading.Thread(target=server); t.start()
            for payload in [b"one", b"", b"\x00two\xff"]:
                send_frame(a, payload, max_frame=100)
                self.assertEqual(recv_frame(a, max_frame=100, timeout=1), payload)
            a.shutdown(socket.SHUT_WR)
            t.join()
            self.assertEqual(result["count"], 3)
        finally:
            a.close(); b.close()

    def test_real_tcp_echo_binary_roundtrip(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(("127.0.0.1", 0)); listener.listen(1)
        port = listener.getsockname()[1]
        result = {}
        def server():
            conn, _ = listener.accept()
            with conn:
                result["count"] = echo_connection(conn, max_frame=100, timeout=1)
            listener.close()
        t = threading.Thread(target=server); t.start()
        with socket.create_connection(("127.0.0.1", port), timeout=1) as client:
            payload = b"\x00abc\xff"
            send_frame(client, payload, max_frame=100)
            self.assertEqual(recv_frame(client, max_frame=100, timeout=1), payload)
        t.join()
        self.assertEqual(result["count"], 1)

    def test_post_green_real_tcp_fragmented_multi_frame(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(("127.0.0.1", 0)); listener.listen(1)
        port = listener.getsockname()[1]
        result = {}
        def server():
            conn, _ = listener.accept()
            with conn:
                result["count"] = echo_connection(conn, max_frame=64, timeout=1)
            listener.close()
        t = threading.Thread(target=server); t.start()
        with socket.create_connection(("127.0.0.1", port), timeout=1) as client:
            raw = encode_frame(b"fragmented", max_frame=64) + encode_frame(b"", max_frame=64) + encode_frame(b"\x00\xff", max_frame=64)
            pos = 0
            for n in [1, 2, 5, 7, 3, 999]:
                if pos >= len(raw):
                    break
                client.sendall(raw[pos:pos+n])
                pos += n
                time.sleep(0.002)
            self.assertEqual(recv_frame(client, max_frame=64, timeout=1), b"fragmented")
            self.assertEqual(recv_frame(client, max_frame=64, timeout=1), b"")
            self.assertEqual(recv_frame(client, max_frame=64, timeout=1), b"\x00\xff")
            client.shutdown(socket.SHUT_WR)
        t.join()
        self.assertEqual(result["count"], 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
