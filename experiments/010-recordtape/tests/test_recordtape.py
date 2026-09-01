import random, struct, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from recordtape import *
from recordtape import _write_all

class PartialWriter:
    def __init__(self, chunk): self.chunk=chunk; self.buf=bytearray(); self.calls=0
    def write(self, view):
        self.calls+=1; n=min(self.chunk,len(view)); self.buf.extend(bytes(view[:n])); return n

class Tests(unittest.TestCase):
    def test_empty_and_multiple(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b""); append_record(p,b"a"); append_record(p,b"\0x")
            self.assertEqual(scan(p).records,(b"",b"a",b"\0x"))
    def _torn_cut(self, cut):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b"one"); append_record(p,b"two")
            base=p.read_bytes(); third=encode_record(b"third"); p.write_bytes(base+third[:cut])
            r=scan(p); self.assertTrue(r.torn_tail); self.assertEqual(r.records,(b"one",b"two"))
            rr=recover(p); self.assertFalse(rr.torn_tail); self.assertEqual(scan(p).records,(b"one",b"two")); self.assertEqual(p.read_bytes(),base)
    def test_partial_header_recover(self): self._torn_cut(3)
    def test_partial_payload_recover(self): self._torn_cut(10)
    def test_partial_checksum_recover(self): self._torn_cut(len(encode_record(b"third"))-2)
    def test_payload_corruption_is_not_repaired(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b"one"); append_record(p,b"two")
            b=bytearray(p.read_bytes()); first_len=len(encode_record(b"one")); b[first_len+8]^=1; p.write_bytes(b); before=p.read_bytes()
            with self.assertRaises(CorruptRecord): recover(p)
            self.assertEqual(p.read_bytes(),before)
    def test_length_corruption_is_not_torn(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b"hello")
            b=bytearray(p.read_bytes()); b[3]^=0x08; p.write_bytes(b); before=p.read_bytes()
            with self.assertRaisesRegex(CorruptRecord,"redundancy"): recover(p)
            self.assertEqual(p.read_bytes(),before)
    def test_oversize_rejected_before_payload(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; n=33; p.write_bytes(struct.pack("!II",n,n^0xffffffff))
            with self.assertRaises(OversizedRecord): scan(p,max_record=32)
    def test_partial_writer(self):
        w=PartialWriter(3); data=encode_record(b"abcdefgh"); _write_all(w,data)
        self.assertEqual(bytes(w.buf),data); self.assertGreater(w.calls,1)
    def test_encode_limit(self):
        with self.assertRaises(ValueError): encode_record(b"1234",max_record=3)
    def test_clean_scan_does_not_modify(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b"x"); before=p.read_bytes(); r=recover(p)
            self.assertEqual(r.records,(b"x",)); self.assertEqual(p.read_bytes(),before)
    def test_post_green_all_torn_cut_points(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"t"; append_record(p,b"A"); append_record(p,b"B"); base=p.read_bytes(); rnd=random.Random(910)
            for size in [0,1,2,7,31,128]:
                payload=bytes(rnd.randrange(256) for _ in range(size)); third=encode_record(payload)
                for cut in range(1,len(third)):
                    p.write_bytes(base+third[:cut]); r=recover(p)
                    self.assertEqual(r.records,(b"A",b"B")); self.assertEqual(p.read_bytes(),base)

if __name__=="__main__": unittest.main(verbosity=2)
