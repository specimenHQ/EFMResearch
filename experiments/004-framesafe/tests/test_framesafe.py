import socket, struct, sys, threading, time, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from framesafe import *

class T(unittest.TestCase):
    def pair(self): return socket.socketpair()
    def test_roundtrip_binary(self):
        a,b=self.pair()
        try: send_frame(a,b'\x00x\xff',8); self.assertEqual(read_frame(b,8),b'\x00x\xff')
        finally: a.close(); b.close()
    def test_empty(self):
        a,b=self.pair()
        try: send_frame(a,b'',0); self.assertEqual(read_frame(b,0),b'')
        finally: a.close(); b.close()
    def test_adjacent(self):
        a,b=self.pair()
        try:
            a.sendall(encode_frame(b'a',8)+encode_frame(b'bc',8))
            self.assertEqual(read_frame(b,8),b'a'); self.assertEqual(read_frame(b,8),b'bc')
        finally: a.close(); b.close()
    def test_clean_eof(self):
        a,b=self.pair(); a.close()
        try: self.assertIsNone(read_frame(b,8))
        finally: b.close()
    def test_partial_header(self):
        a,b=self.pair(); a.sendall(b'\x00\x00'); a.close()
        try:
            with self.assertRaises(FrameTruncated): read_frame(b,8)
        finally: b.close()
    def test_partial_payload(self):
        a,b=self.pair(); a.sendall(struct.pack('!I',4)+b'ab'); a.close()
        try:
            with self.assertRaises(FrameTruncated): read_frame(b,8)
        finally: b.close()
    def test_exact_max_and_plus_one(self):
        a,b=self.pair()
        try: send_frame(a,b'12345678',8); self.assertEqual(read_frame(b,8),b'12345678')
        finally: a.close(); b.close()
        a,b=self.pair(); a.sendall(struct.pack('!I',9))
        try:
            with self.assertRaises(FrameTooLarge): read_frame(b,8,timeout=.05)
        finally: a.close(); b.close()
    def test_fragmented_header_and_payload(self):
        a,b=self.pair(); wire=encode_frame(b'abcdef',16)
        def tx():
            for byte in wire:
                a.sendall(bytes([byte])); time.sleep(.002)
            a.close()
        t=threading.Thread(target=tx); t.start()
        try: self.assertEqual(read_frame(b,16,timeout=.2),b'abcdef')
        finally: t.join(); b.close()
    def test_total_deadline(self):
        a,b=self.pair()
        def tx():
            try:
                a.sendall(struct.pack('!I',4))
                for ch in b'abcd': time.sleep(.06); a.sendall(bytes([ch]))
            except OSError: pass
            finally: a.close()
        t=threading.Thread(target=tx); t.start()
        try:
            with self.assertRaises(FrameTimeout): read_frame(b,8,timeout=.12)
        finally: t.join(); b.close()
    def test_oversize_rejected_without_payload(self):
        a,b=self.pair(); a.sendall(struct.pack('!I',100))
        try:
            start=time.monotonic()
            with self.assertRaises(FrameTooLarge): read_frame(b,8,timeout=.2)
            self.assertLess(time.monotonic()-start,.1)
        finally: a.close(); b.close()
    def test_first_frame_survives_second_frame_timeout(self):
        a,b=self.pair()
        def tx():
            try:
                a.sendall(encode_frame(b'first',16)); a.sendall(struct.pack('!I',5)+b'x'); time.sleep(.2)
            except OSError: pass
            finally: a.close()
        t=threading.Thread(target=tx); t.start()
        try:
            self.assertEqual(read_frame(b,16,timeout=.1),b'first')
            with self.assertRaises(FrameTimeout): read_frame(b,16,timeout=.05)
        finally: t.join(); b.close()

if __name__=='__main__': unittest.main(verbosity=2)
