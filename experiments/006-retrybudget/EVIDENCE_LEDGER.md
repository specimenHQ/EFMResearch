# Evidence Ledger — Experiment 006 RetryBudget

| ID | Evidence | Strength | Decision |
|---|---|---|---|
| A1 | monotonic elapsed boundary behaved as required in controlled probe | E2 | monotonic clock retained |
| A2 | retryable subclass matched; unrelated exception did not | E2 → E5 | exception classes are retry authority |
| A3 | falsy successful values exercised in integration | E2 → E5 | return truthiness never controls retry |
| A4 | fixed 0.5 sleep from t=.7 overshot t=1 deadline | E2 → E5 | clip backoff and recheck deadline |
| A5 | injected fake clock/sleep deterministically exercised boundaries | E2 → E5 | dependency injection retained; no threads needed |
| A6 | running callable exceeded scheduling budget | E2 | no hard cancellation claim |
| J0 | initial exact-float assertion falsely rejected known-good behavior | E2 observation | evaluator corrected before acceptance |
| J1 | 5/5 known-false implementations rejected | E3 | judge accepted |
| I1 | 10/10 integration + independent post-green oversleep challenge pass | E5 | implementation accepted |

No E6 claim.
