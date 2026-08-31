# Preimplementation Results — Protocol v0.2

- **A1 PASS (E2):** `recv(4)` returned one byte when only one byte was available.
- **A2 PASS (E2):** adjacent frames, an empty frame, and binary bytes were separated by a 4-byte length prefix.
- **A3 PASS (E2):** clean EOF before a header was distinguishable from EOF in a partial header or payload.
- **A4 PASS (E2):** exact-max payload was accepted; max+1 was rejected from the header without payload.
- **A5 PASS (E2):** `struct !I` encoded `0x01020304` as `01 02 03 04`.
- **A6 PASS (E2):** a 0.10s per-read socket timeout allowed a slow 4-byte read to complete in ~0.28s, proving it is not a total frame deadline.

Earned design: exact-read loop, 4-byte network-order length prefix, explicit clean/truncated EOF distinction, header-time size rejection, and a monotonic total-frame deadline.
