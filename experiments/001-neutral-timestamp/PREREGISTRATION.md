# EFM Neutral Pilot — Preregistration

## Selection
Candidate tasks were fixed before random selection:
1. unicode_deduper
2. interval_coverage
3. decimal_cart_total
4. iso8601_sorter
5. path_containment

Selected by Python `secrets.choice`: `iso8601_sorter`.

## Task
Implement `sort_timestamps(values)`.

Requirements:
- Input: a sequence of ISO-8601 timestamp strings.
- Every accepted timestamp must contain timezone information (`Z` or a numeric UTC offset).
- Return the original strings sorted from earliest instant to latest instant.
- Different textual timestamps denoting the same instant must retain their original relative order.
- Fractional seconds are allowed.
- Input may be unsorted and may cross date boundaries.
- A timestamp without timezone information must be rejected with `ValueError`.
- Do not mutate the caller's input sequence.

## Arms
### A — Build-first
Implement directly from the task. No exploratory/microtests before freezing the first implementation.

### B — EFM
Before implementation:
1. list assumptions;
2. rank consequential uncertainty;
3. run the smallest falsifiable microtests on the runtime/library behavior relied upon;
4. implement only after those results.

## Common evaluation
After both first implementations are frozen by SHA-256, generate a fresh common adversarial suite and run both implementations unchanged.

Metrics:
- initial common-suite failures;
- implementation LOC;
- preimplementation experiment count;
- rework needed after common evaluation;
- important assumptions resolved before implementation;
- whether EFM changed the implementation decision.

## Interpretation
This is a pilot, not proof. The same investigator specifies and implements both arms, so there is no blinding or independent replication.
