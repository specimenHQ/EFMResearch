import socket, struct, threading, time


def recv_exact(sock, n):
    out = bytearray()
    while len(out) < n:
        b = sock.recv(n - len(out))
        if not b:
            raise EOFError
        out += b
    return bytes(out)


def frame(payload):
    return struct.pack('!I', len(payload)) + payload

# A1: recv(n) may return fewer than n bytes without EOF.
a,b = socket.socketpair()
try:
    a.sendall(b'ab')
    got = b.recv(4)
    assert got == b'ab'
finally:
    a.close(); b.close()
print('A1 PASS partial recv observed')

# A2 + neighboring empty/adjacent cases.
a,b = socket.socketpair()
try:
    a.sendall(frame(b'') + frame(b'xyz'))
    n1 = struct.unpack('!I', recv_exact(b,4))[0]
    p1 = recv_exact(b,n1)
    n2 = struct.unpack('!I', recv_exact(b,4))[0]
    p2 = recv_exact(b,n2)
    assert (p1,p2) == (b'',b'xyz')
finally:
    a.close(); b.close()
print('A2 PASS adjacent frames and empty payload separated')

# A3: clean EOF before header differs from partial header EOF.
a,b = socket.socketpair(); a.close()
assert b.recv(4) == b''; b.close()
a,b = socket.socketpair(); a.sendall(b'\x00\x00'); a.close()
assert b.recv(4) == b'\x00\x00'; b.close()
print('A3 PASS clean EOF and partial-header EOF are distinguishable')

# A4: declared oversize is knowable from header alone.
max_payload=8
hdr = struct.pack('!I', max_payload+1)
assert struct.unpack('!I', hdr)[0] > max_payload
print('A4 PASS oversize detectable from header before payload read')

# A5: network-order unsigned 32-bit field round trips boundaries.
for n in (0,1,255,256,65535,2**32-1):
    assert struct.unpack('!I', struct.pack('!I', n))[0] == n
print('A5 PASS !I stable for tested uint32 boundaries')

# A6: a per-read socket timeout is not a total-frame deadline.
a,b = socket.socketpair()
b.settimeout(0.10)
def sender():
    a.sendall(struct.pack('!I',4))
    for ch in b'abcd':
        time.sleep(0.06)
        a.sendall(bytes([ch]))
t = threading.Thread(target=sender); t.start()
start=time.monotonic()
try:
    recv_exact(b,4)
    payload=recv_exact(b,4)
    elapsed=time.monotonic()-start
    assert payload == b'abcd' and elapsed > 0.20
finally:
    t.join(); a.close(); b.close()
print(f'A6 PASS per-read timeout allowed total frame time {elapsed:.3f}s > 0.10s')
