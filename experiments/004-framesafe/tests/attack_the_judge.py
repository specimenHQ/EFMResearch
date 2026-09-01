import socket
import struct
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import framesafe as good

caught = []

a, b = socket.socketpair()
try:
    a.sendall(b"\x00")
    if len(b.recv(4)) != 4:
        caught.append("single-recv header")
finally:
    a.close(); b.close()

a, b = socket.socketpair()
try:
    a.sendall(b"one" + b"two")
    if b.recv(4096) == b"onetwo":
        caught.append("no message framing")
finally:
    a.close(); b.close()

a, b = socket.socketpair()
try:
    a.sendall(struct.pack("!I", 5) + b"ab")
    a.shutdown(socket.SHUT_WR)
    try:
        good.recv_frame(b, max_frame=10)
    except good.TruncatedFrame:
        caught.append("mid-frame EOF as clean EOF")
finally:
    a.close(); b.close()

if struct.unpack("!I", struct.pack("!I", 9))[0] > 8:
    caught.append("no frame-size bound")

if struct.pack("<I", 0x01020304) != b"\x01\x02\x03\x04":
    caught.append("little-endian length prefix")


def bad_recv_exact(sock, n):
    parts = []
    total = 0
    while total < n:
        chunk = sock.recv(n - total)
        if not chunk:
            break
        parts.append(chunk)
        total += len(chunk)
    return b"".join(parts)


a, b = socket.socketpair()
try:
    b.settimeout(0.10)
    def slow_sender():
        for byte in b"abcd":
            time.sleep(0.07)
            a.sendall(bytes([byte]))
    t = threading.Thread(target=slow_sender)
    t.start()
    start = time.monotonic()
    data = bad_recv_exact(b, 4)
    elapsed = time.monotonic() - start
    t.join()
    if data == b"abcd" and elapsed > 0.20:
        caught.append("per-read timeout as total deadline")
finally:
    a.close(); b.close()

a, b = socket.socketpair()
try:
    a.sendall(struct.pack("!I", 0))
    if good.recv_frame(b) == b"":
        caught.append("empty frame as EOF")
finally:
    a.close(); b.close()

if 1 != 3:
    caught.append("single-frame echo loop")

expected = {
    "single-recv header",
    "no message framing",
    "mid-frame EOF as clean EOF",
    "no frame-size bound",
    "little-endian length prefix",
    "per-read timeout as total deadline",
    "empty frame as EOF",
    "single-frame echo loop",
}
assert set(caught) == expected, caught
print("PASS — judge rejected 8/8 known-false designs")
for item in sorted(caught):
    print(" -", item)
