# Outcome — Experiment 004 FrameSafe

FrameSafe is the first Protocol v0.2 EFM-native build and the first networking-domain study.

## Result

EFM materially constrained the design before code:
- A1 falsified the assumption that one `recv(n)` is a complete read.
- A6 falsified the assumption that a per-read timeout is a total frame deadline.
- A2–A5 established the minimum framing, EOF, size-bound, and byte-order behavior.

The first integrated implementation passed. Protocol v0.2 then required a non-replayed post-green challenge: a real localhost TCP stream carrying three messages was deliberately fragmented/coalesced. It also passed without rework.

The adversarial judge rejected 8/8 false designs, including near misses for little-endian framing, per-read timeout semantics, and empty-frame/EOF confusion.

## Interpretation

This is a useful non-defect result. EFM changed architecture before implementation but did not discover a defect after implementation. It therefore supports the claim that EFM can constrain design without requiring every run to produce a rejected build.

Final evidence: E5 integration. No E6 claim and no comparison against build-first.
