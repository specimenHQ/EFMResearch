# Assumption Register — Initial State (Protocol v0.2)

| ID | Importance | Assumption | Claim scope | Before test |
|---|---|---|---|---|
| A1 | Existential | `recv(n)` may return fewer than n bytes without EOF | blocking local TCP/socketpair reads | E0 |
| A2 | Architectural | a fixed 4-byte length prefix can separate back-to-back binary messages | frames up to configured maximum | E0 |
| A3 | Operational | EOF before any header byte can mean clean end, while EOF after any frame byte must be an error | one connection, sequential framed reads | E0 |
| A4 | Operational | oversized length can be rejected from the header before payload allocation/read | declared length > configured max | E0 |
| A5 | Architectural | `struct !I` provides a stable unsigned 32-bit network-order length field | Python peers using stdlib `struct` | E0 |
| A6 | Operational | a socket per-read timeout is not necessarily a total frame deadline | slow multi-chunk frame on one connection | E0 |

For each broader claim, neighboring cases must be tested before promotion: empty payload, adjacent frames, partial header, partial payload, exact-max payload, max+1 payload.
