# Final Record — Experiment 009 ZipGuard

Protocol: v0.2 unchanged. Track: clean EFM-native. Goal/decision/assumptions were frozen before tests.

## Evidence
A1 E2→E5: traversal/absolute/backslash member hazards rejected. A2 E2→E5: pre-existing symlink parent defeats pathname containment. A3 E2→E5: ZIP symlink metadata detectable and rejected. A4 E2→E5: normalized duplicates/type collisions require whole-archive validation. A5 E2→E5: exclusive creation preserves existing files. A6 E2→E5: archive-structure failures validate before writes. A7 E2→E5: validate-then-open pathname race wrote outside root; architecture changed to descriptor-relative `O_DIRECTORY|O_NOFOLLOW` traversal and `O_CREAT|O_EXCL|O_NOFOLLOW` final creation. Judge E3: 5/5 false variants rejected. Integration E5: 11/11 plus injected symlink-swap challenge passed.

## Metrics
Initial assumptions: 6; newly admitted dangerous assumption: 1. Consequential prebuild falsification: 1 (A7). Implementation logical LOC: 133. Integration: 11/11. Judge: 5/5. Third-party dependencies: 0. Accepted implementation: yes within tested POSIX scope. Evidence ceiling: E5; no E6.

## Outcome
EFM materially changed architecture before implementation. The original validate-then-open approach was not accepted after a controlled race demonstrated an outside-root write. The final descriptor-relative design survived integration and post-green adversarial testing without further rework.

Scope limitation: no claim against a separate hostile process relocating already-open directories outside the root, ZIP bombs/disk exhaustion, non-POSIX platforms, or operational use.
