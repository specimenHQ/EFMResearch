#!/usr/bin/env python3
from __future__ import annotations

import argparse
import socket
import struct
import sys
import time
from contextlib import contextmanager

HEADER_SIZE = 4
UINT32_MAX = 0xFFFFFFFF
DEFAULT_MAX_FRAME = 1024 * 1024


class FrameError(Exception):
    pass


class TruncatedFrame(FrameError):
    pass


class OversizedFrame(FrameError):
    pass


class FrameTimeout(FrameError):
    pass


def _validate_max(max_frame: int) -> None:
    if not isinstance(max_frame, int) or isinstance(max_frame, bool):
        raise ValueError("max_frame must be an integer")
    if not 0 <= max_frame <= UINT32_MAX:
        raise ValueError("max_frame must be between 0 and 2^32-1")


@contextmanager
def _temporary_timeout(sock: socket.socket, timeout: float | None):
    original = sock.gettimeout()
    try:
        sock.settimeout(timeout)
        yield
    finally:
        sock.settimeout(original)


def _recv_exact(
    sock: socket.socket,
    n: int,
    *,
    deadline: float | None,
    clean_eof_ok: bool = False,
) -> bytes | None:
    parts: list[bytes] = []
    remaining = n
    while remaining:
        timeout = None
        if deadline is not None:
            timeout = deadline - time.monotonic()
            if timeout <= 0:
                raise FrameTimeout("total frame deadline exceeded")
        try:
            with _temporary_timeout(sock, timeout):
                chunk = sock.recv(remaining)
        except socket.timeout as exc:
            raise FrameTimeout("total frame deadline exceeded") from exc
        if not chunk:
            if clean_eof_ok and not parts:
                return None
            received = n - remaining
            raise TruncatedFrame(f"EOF after {received} of {n} required bytes")
        parts.append(chunk)
        remaining -= len(chunk)
    return b"".join(parts)


def encode_frame(payload: bytes | bytearray | memoryview, *, max_frame: int = DEFAULT_MAX_FRAME) -> bytes:
    _validate_max(max_frame)
    data = bytes(payload)
    if len(data) > max_frame:
        raise OversizedFrame(f"payload size {len(data)} exceeds maximum {max_frame}")
    return struct.pack("!I", len(data)) + data


def send_frame(
    sock: socket.socket,
    payload: bytes | bytearray | memoryview,
    *,
    max_frame: int = DEFAULT_MAX_FRAME,
) -> None:
    sock.sendall(encode_frame(payload, max_frame=max_frame))


def recv_frame(
    sock: socket.socket,
    *,
    max_frame: int = DEFAULT_MAX_FRAME,
    timeout: float | None = None,
) -> bytes | None:
    _validate_max(max_frame)
    if timeout is not None and timeout <= 0:
        raise ValueError("timeout must be > 0 or None")
    deadline = None if timeout is None else time.monotonic() + timeout

    header = _recv_exact(sock, HEADER_SIZE, deadline=deadline, clean_eof_ok=True)
    if header is None:
        return None

    (length,) = struct.unpack("!I", header)
    if length > max_frame:
        raise OversizedFrame(f"declared frame size {length} exceeds maximum {max_frame}")

    payload = _recv_exact(sock, length, deadline=deadline)
    assert payload is not None
    return payload


def echo_connection(
    conn: socket.socket,
    *,
    max_frame: int = DEFAULT_MAX_FRAME,
    timeout: float | None = None,
) -> int:
    count = 0
    while True:
        payload = recv_frame(conn, max_frame=max_frame, timeout=timeout)
        if payload is None:
            return count
        send_frame(conn, payload, max_frame=max_frame)
        count += 1


def serve_once(
    host: str,
    port: int,
    *,
    max_frame: int = DEFAULT_MAX_FRAME,
    timeout: float | None = None,
) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(1)
        actual_port = listener.getsockname()[1]
        print(f"LISTENING {actual_port}", flush=True)
        conn, _ = listener.accept()
        with conn:
            return echo_connection(conn, max_frame=max_frame, timeout=timeout)


def roundtrip(
    host: str,
    port: int,
    payload: bytes,
    *,
    max_frame: int = DEFAULT_MAX_FRAME,
    timeout: float | None = None,
) -> bytes:
    with socket.create_connection((host, port), timeout=timeout) as sock:
        send_frame(sock, payload, max_frame=max_frame)
        result = recv_frame(sock, max_frame=max_frame, timeout=timeout)
        if result is None:
            raise TruncatedFrame("peer closed before echo response")
        return result


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Length-prefixed local TCP framing tool")
    sub = p.add_subparsers(dest="command", required=True)

    serve = sub.add_parser("serve")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=9009)
    serve.add_argument("--max-frame", type=int, default=DEFAULT_MAX_FRAME)
    serve.add_argument("--timeout", type=float, default=None)

    send = sub.add_parser("send")
    send.add_argument("host")
    send.add_argument("port", type=int)
    send.add_argument("payload", help="UTF-8 text unless --hex")
    send.add_argument("--hex", action="store_true")
    send.add_argument("--max-frame", type=int, default=DEFAULT_MAX_FRAME)
    send.add_argument("--timeout", type=float, default=None)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "serve":
            serve_once(args.host, args.port, max_frame=args.max_frame, timeout=args.timeout)
            return 0
        payload = bytes.fromhex(args.payload) if args.hex else args.payload.encode()
        reply = roundtrip(
            args.host, args.port, payload,
            max_frame=args.max_frame, timeout=args.timeout
        )
        if args.hex:
            print(reply.hex())
        else:
            print(reply.decode())
        return 0
    except (FrameError, OSError, ValueError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
