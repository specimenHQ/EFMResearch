# Outcome — Experiment 010 RecordTape

Status: accepted within frozen scope at E5.

EFM changed the architecture twice before implementation. Length-only framing could not detect a payload bit flip. Adding CRC was still insufficient operationally because an upward corruption of the leading length could make the reader run out of bytes before locating the checksum, falsely resembling a torn tail. The evidence-earned format therefore stores redundant pre-payload length metadata `(length, length XOR 0xffffffff)` and a CRC32 over header+payload.

The implementation then passed 11/11 integration tests, including preservation of complete corruption evidence, bounded size rejection, partial-write simulation, and recovery of prior valid records. The post-green challenge exercised every nonempty cut point of a third record for six payload sizes; recovery always preserved exactly the first two records. The judge rejected 5/5 known-false designs.

Scope remains deliberately narrow: single writer, local regular file, process-level torn writes. No claim is made about CRC collision resistance, concurrent writers, device write ordering, fsync semantics, or power-loss durability.
