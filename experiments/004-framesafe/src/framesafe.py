import select
import socket
import struct
import time

HEADER_SIZE = 4
UINT32_MAX = 2**32 - 1

class FrameError(Exception): pass
class FrameTruncated(FrameError): pass
class FrameTooLarge(FrameError): pass
class FrameTimeout(FrameError): pass


def encode_frame(payload: bytes, max_payload: int) -> bytes:
    if not isinstance(payload, (bytes, bytearray, memoryview)):
        raise TypeError('payload must be bytes-like')
    payload = bytes(payload)
    if max_payload < 0 or max_payload > UINT32_MAX:
        raise ValueError('invalid max_payload')
    if len(payload) > max_payload:
        raise FrameTooLarge(f'{len(payload)} > {max_payload}')
    return struct.pack('!I', len(payload)) + payload


def _recv_exact(sock: socket.socket, n: int, *, deadline: float | None, allow_clean_eof: bool=False):
    out = bytearray()
    while len(out) < n:
        if deadline is not None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise FrameTimeout('frame deadline exceeded')
            readable, _, _ = select.select([sock], [], [], remaining)
            if not readable:
                raise FrameTimeout('frame deadline exceeded')
        chunk = sock.recv(n - len(out))
        if not chunk:
            if not out and allow_clean_eof:
                return None
            raise FrameTruncated(f'EOF after {len(out)} of {n} bytes')
        out += chunk
    return bytes(out)


def read_frame(sock: socket.socket, max_payload: int, *, timeout: float | None=None):
    if max_payload < 0 or max_payload > UINT32_MAX:
        raise ValueError('invalid max_payload')
    if timeout is not None and timeout < 0:
        raise ValueError('timeout must be nonnegative')
    deadline = None if timeout is None else time.monotonic() + timeout
    header = _recv_exact(sock, HEADER_SIZE, deadline=deadline, allow_clean_eof=True)
    if header is None:
        return None
    length = struct.unpack('!I', header)[0]
    if length > max_payload:
        raise FrameTooLarge(f'{length} > {max_payload}')
    if length == 0:
        return b''
    return _recv_exact(sock, length, deadline=deadline, allow_clean_eof=False)


def send_frame(sock: socket.socket, payload: bytes, max_payload: int) -> None:
    sock.sendall(encode_frame(payload, max_payload))
