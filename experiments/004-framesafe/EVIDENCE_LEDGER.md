# Evidence Ledger — Experiment 004 FrameSafe

Protocol: v0.2

| ID | Evidence | Strength | Decision |
|---|---|---|---|
| A1 | one-byte availability caused `recv(4)` to return one byte | E2 | exact-read loop required |
| A2 | adjacent, empty, and binary frames separated under 4-byte prefix | E2 | fixed length prefix retained |
| A3 | clean EOF, partial header, and partial payload produced distinct outcomes | E2 → E5 | clean EOF returns `None`; partial frame raises `TruncatedFrame` |
| A4 | exact-max accepted; max+1 rejected from header | E2 → E5 | reject oversize before payload read |
| A5 | `!I` produced network-order bytes `01 02 03 04` | E2 | use network byte order |
| A6 | 0.10s per-read timeout allowed ~0.28s slow read | E2 → E5 | implement monotonic total-frame deadline |
| J1 | 8 deliberately false/near-miss designs rejected | E3 | judge hardened |
| I1 | real localhost TCP with fragmented/coalesced three-frame stream passed after first green suite | E5 | integration claim retained |

No E6 operational evidence is claimed.
