# Preimplementation Results — RecordTape

- A1 FALSIFIED: length+payload framing silently accepts a single-bit payload mutation because size remains valid.
- A2 PARTIALLY FALSIFIED / architecture changed: CRC over length+payload detects mutations only if the checksum can be located. A single-bit length mutation 5→13 makes a complete 13-byte record appear short before the reader reaches the CRC. CRC alone therefore cannot reliably distinguish that corruption from a torn tail.
- Corrective probe PASS: redundant pre-payload metadata `(length, length XOR 0xffffffff)` detects the tested single-bit length mutation before payload read; CRC over redundant header+payload detects tested payload mutation.
- A3 PASS within scoped fixtures: partial header, partial payload, and partial checksum are structurally distinguishable from a complete checksum failure when redundant header validates.
- A4 PASS: bounded write-all loop reproduced partial 3-byte writes and reconstructed the exact record without altering prior bytes.
- A5 PASS: with two complete records plus a torn third, the last verified offset equals exactly the end of record two.
- A6 PASS: oversized declared length is rejectable immediately after a valid redundant header, before payload read.

Evidence: E2. No collision-proof or power-loss durability claim.