# Metrics — Experiment 003 MergeSafe

- Research track: `native`
- Protocol: `0.1 — Frozen for initial replication`
- Initial assumptions admitted: 6
- New dangerous assumptions admitted during the run: 3 (A7, A8, A9)
- Total assumption IDs investigated: 9
- Third-party runtime dependencies: 0
- Judge falsifications attempted: 7
- Judge falsifications rejected: 7
- Judge falsifications accepted: 0
- Judge false-acceptance rate on constructed falsifications: `0 / 7`
- Final integration tests: 12 passing / 0 failing
- Rejected implementation retained: yes (`history/mergesafe_v0_rejected.py`)
- Implementation v0 physical / nonblank-noncomment LOC: 141 / 108
- Implementation v0.1 physical / nonblank-noncomment LOC: 191 / 151
- v0 → v0.1 implementation change: 58 added / 8 removed lines
- Integration-test physical / nonblank-noncomment LOC: 142 / 123
- Judge-attack physical / nonblank-noncomment LOC: 92 / 81
- Initial prebuild microtest code physical / nonblank-noncomment LOC: 107 / 88
- A7 microtest physical / nonblank-noncomment LOC: 23 / 20
- A8/A9 microtest physical / nonblank-noncomment LOC: 61 / 46
- Consequential defects/false assumptions found before meaningful implementation: 1 operational (A7)
- Consequential defects/false assumptions found after first integration during judge hardening: 1 architectural (A8), 1 operational (A9)
- Architecture decisions materially changed by evidence: yes
- Final evidence level reached: E5
- E6 representative-use evidence: none
- Wall-clock active-work, token, and dollar cost: not independently instrumented; no numeric claim made

## Interpretation boundary

These counts describe one experiment. They are not a composite EFM score and are not statistical evidence of methodology superiority.
