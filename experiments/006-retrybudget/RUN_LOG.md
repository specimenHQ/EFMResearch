# Run Log — Experiment 006

1. Goal, decision map, assumption register, and claim scopes were durably committed before microtests (`04d8a2829c8538ded6196aba99690a4778f06d2b`).
2. A1–A6 controlled probes executed; A4 constrained backoff/deadline design; A6 constrained claim scope.
3. Minimal stdlib implementation written.
4. First integration run: 9 pass / 1 false rejection caused by exact float assertion (`0.30000000000000004 != 0.3`).
5. Judge corrected to tolerance-based float comparison; no application code changed for that failure.
6. Final integration: 10/10 pass.
7. Post-green challenge: injected sleep overshot requested delay; implementation rechecked clock and started no late retry.
8. Judge attack: 5/5 known-false implementations rejected.
9. Accepted at E5; no E6 claim.
