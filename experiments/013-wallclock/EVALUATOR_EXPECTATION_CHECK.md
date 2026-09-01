# Evaluator Expectation Check — Experiment 013 WallClock

Protocol v0.3 requires an independent check before nontrivial expected values are used to blame the implementation.

## Fixed-offset arithmetic

The UTC expectations used by the integration suite were independently derived from explicit fixed offsets rather than from the candidate classifier:

- winter: `2026-01-15 09:00 -05:00` → `14:00 UTC`;
- summer: `2026-07-15 09:00 -04:00` → `13:00 UTC`;
- first fall-back occurrence: `2026-11-01 01:30 -04:00` → `05:30 UTC`;
- second fall-back occurrence: `2026-11-01 01:30 -05:00` → `06:30 UTC`.

All matched the integration expectations.

## Transition-boundary check

A separate UTC→local observation established the tested gap/repeat boundaries without using the candidate local-time classifier:

- `2026-03-08 06:59 UTC` → `01:59 -05:00`;
- `2026-03-08 07:00 UTC` → `03:00 -04:00`;
- therefore the local `02:xx` hour is absent at the tested spring transition;
- `2026-11-01 05:59 UTC` → `01:59 -04:00`;
- `2026-11-01 06:00 UTC` → `01:00 -05:00`;
- therefore the local `01:xx` hour repeats at the tested fall transition.

Result: evaluator expectations accepted before candidate integration results were interpreted.
