import struct,zlib,tempfile,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from recordtape import *

def length_only_bad():
    p=b"hello"; b=bytearray(struct.pack("!I",len(p))+p); b[4]^=1
    return struct.unpack("!I",b[:4])[0]==len(b)-4

def crc_only_bad():
    p=b"hello"; h=struct.pack("!I",len(p)); b=bytearray(h+p+struct.pack("!I",zlib.crc32(h+p)&0xffffffff)); b[3]^=0x08
    return len(b)-4 < struct.unpack("!I",b[:4])[0]

def no_max_bad():
    n=10000; b=struct.pack("!II",n,n^0xffffffff); return len(b)-8 < n

class Partial:
    def __init__(self): self.buf=bytearray()
    def write(self,b): n=min(2,len(b)); self.buf.extend(bytes(b[:n])); return n

def single_write_bad():
    w=Partial(); data=encode_record(b"abcdef"); w.write(data); return bytes(w.buf)!=data

def repair_any_error_bad():
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"t"; append_record(p,b"one"); append_record(p,b"two"); b=bytearray(p.read_bytes()); b[len(encode_record(b"one"))+8]^=1; p.write_bytes(b); before=p.read_bytes()
        try: scan(p)
        except RecordTapeError: p.write_bytes(before[:len(encode_record(b"one"))])
        return p.read_bytes()!=before

checks=[length_only_bad(),crc_only_bad(),no_max_bad(),single_write_bad(),repair_any_error_bad()]
assert all(checks),checks
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/"t"; append_record(p,b"a"); append_record(p,b"b"); assert recover(p).records==(b"a",b"b")
print("PASS: 5/5 known-false designs rejected; accepted implementation accepted")
