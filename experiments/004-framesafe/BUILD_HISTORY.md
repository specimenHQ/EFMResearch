# Build History — Experiment 004

## v0 — accepted at E5

Preimplementation evidence directly determined:
- exact-read loop;
- 4-byte network-order length prefix;
- explicit truncated-frame errors;
- header-time size rejection;
- monotonic total-frame deadline.

The first integrated implementation passed the initial suite. Protocol v0.2 required a distinct post-green integration challenge before E5; that challenge also passed.

No implementation was discarded or reworked. This is retained as a valid outcome rather than manufacturing a defect.
