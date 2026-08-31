# Outcome — Experiment 004 FrameSafe

Protocol: v0.2.

Result: EFM constrained the design before implementation. The consequential finding was A6: a socket per-read timeout can allow a frame to exceed the intended total time budget, so the implementation uses one monotonic deadline across header + payload reads.

Final evidence:
- preimplementation assumptions: 6/6 reproduced at E2;
- integration: 11/11 pass;
- judge attack: 7/7 known-false candidates rejected;
- post-green challenge: first complete frame remains valid when the following frame stalls and times out;
- dependencies: 0 third-party;
- evidence ceiling: E5; no E6 claim.

No additional implementation defect was found after the first green integration suite. This is retained as a non-defect result rather than treated as a forced EFM win.
