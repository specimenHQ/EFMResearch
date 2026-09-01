# Assumption Register — RecordTape

| ID | Class | Assumption | Claim scope |
|---|---|---|---|
| A1 | Architectural | length+payload framing alone cannot detect payload corruption | single-bit payload mutation of a complete record |
| A2 | Architectural | CRC32 over header+payload detects tested payload and length mutations | controlled single-bit mutations; not a collision-proof claim |
| A3 | Operational | incomplete final header/payload/checksum is distinguishable from checksum failure on a complete record | sequential scan of one file |
| A4 | Operational | a bounded write-all loop can represent process-level partial writes without losing prior records | single writer, regular file |
| A5 | Operational | truncating only to last verified offset restores a file with an incomplete final record | final-record truncations only |
| A6 | Operational | validating declared length against a fixed maximum before reading payload prevents unbounded allocation/read | malformed complete header |

Neighbor cases: zero-length record, partial header, partial payload, partial checksum, payload bit flip, length bit flip, oversized declared length, two valid records followed by torn third.