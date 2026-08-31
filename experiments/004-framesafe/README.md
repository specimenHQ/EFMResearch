# Experiment 004 — FrameSafe

Protocol v0.2 EFM-native networking build.

Critical invariant: TCP chunking/coalescing must never change message boundaries or bytes; truncated and oversized frames must not be accepted as complete.

Final:
- 6 preimplementation microtests;
- 11/11 integration tests;
- 8/8 judge mutants rejected;
- 1 post-green real-TCP fragmentation challenge passed;
- 0 third-party dependencies;
- E5, no E6.

Run:

```bash
python -m unittest discover -s tests -p 'test_framesafe.py' -v
python tests/attack_the_judge.py
```
