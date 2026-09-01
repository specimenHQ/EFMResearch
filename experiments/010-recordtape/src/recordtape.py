from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import struct
import zlib

HEADER_FMT = "!II"
HEADER_SIZE = struct.calcsize(HEADER_FMT)
CHECKSUM_SIZE = 4
DEFAULT_MAX_RECORD = 1024 * 1024
MASK32 = 0xFFFFFFFF

class RecordTapeError(Exception):
    pass

class CorruptRecord(RecordTapeError):
    def __init__(self, offset: int, reason: str):
        super().__init__(f"corrupt record at offset {offset}: {reason}")
        self.offset = offset
        self.reason = reason

class OversizedRecord(CorruptRecord):
    pass

@dataclass(frozen=True)
class ScanResult:
    records: tuple[bytes, ...]
    last_verified_offset: int
    torn_tail: bool

def _validate_max(max_record: int) -> None:
    if not isinstance(max_record, int) or isinstance(max_record, bool) or not (0 <= max_record <= MASK32):
        raise ValueError("max_record must be an integer in [0, 2^32-1]")

def _header(length: int) -> bytes:
    return struct.pack(HEADER_FMT, length, length ^ MASK32)

def encode_record(payload: bytes | bytearray | memoryview, *, max_record: int = DEFAULT_MAX_RECORD) -> bytes:
    _validate_max(max_record)
    data = bytes(payload)
    if len(data) > max_record:
        raise ValueError("payload exceeds max_record")
    h = _header(len(data))
    checksum = zlib.crc32(h + data) & MASK32
    return h + data + struct.pack("!I", checksum)

def _write_all(writer, data: bytes) -> None:
    view = memoryview(data)
    pos = 0
    while pos < len(view):
        written = writer.write(view[pos:])
        if written is None or written <= 0:
            raise OSError("write made no progress")
        pos += written

def append_record(path: str | Path, payload: bytes | bytearray | memoryview, *, max_record: int = DEFAULT_MAX_RECORD) -> int:
    blob = encode_record(payload, max_record=max_record)
    with open(path, "ab", buffering=0) as f:
        start = f.tell()
        _write_all(f, blob)
        return start + len(blob)

def scan(path: str | Path, *, max_record: int = DEFAULT_MAX_RECORD) -> ScanResult:
    _validate_max(max_record)
    records: list[bytes] = []
    last_verified = 0
    with open(path, "rb") as f:
        while True:
            start = f.tell()
            h = f.read(HEADER_SIZE)
            if not h:
                return ScanResult(tuple(records), last_verified, False)
            if len(h) < HEADER_SIZE:
                return ScanResult(tuple(records), last_verified, True)
            length, inverse = struct.unpack(HEADER_FMT, h)
            if (length ^ inverse) != MASK32:
                raise CorruptRecord(start, "length redundancy mismatch")
            if length > max_record:
                raise OversizedRecord(start, f"declared length {length} exceeds maximum {max_record}")
            payload = f.read(length)
            if len(payload) < length:
                return ScanResult(tuple(records), last_verified, True)
            checksum_bytes = f.read(CHECKSUM_SIZE)
            if len(checksum_bytes) < CHECKSUM_SIZE:
                return ScanResult(tuple(records), last_verified, True)
            stored = struct.unpack("!I", checksum_bytes)[0]
            actual = zlib.crc32(h + payload) & MASK32
            if stored != actual:
                raise CorruptRecord(start, "checksum mismatch")
            records.append(payload)
            last_verified = f.tell()

def recover(path: str | Path, *, max_record: int = DEFAULT_MAX_RECORD) -> ScanResult:
    result = scan(path, max_record=max_record)
    if not result.torn_tail:
        return result
    with open(path, "r+b", buffering=0) as f:
        f.truncate(result.last_verified_offset)
    return ScanResult(result.records, result.last_verified_offset, False)
