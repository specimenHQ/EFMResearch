# Assumption Register — Initial State (Protocol v0.2)

| ID | Importance | Assumption | Claim scope | Before test |
|---|---|---|---|---|
| A1 | Architectural | a monotonic clock is the correct authority for elapsed retry budget | elapsed scheduling time within one process | E0 |
| A2 | Operational | retryable vs nonretryable failures can be decided by configured exception classes | synchronous Python exceptions raised by the callable | E0 |
| A3 | Operational | successful falsy return values must terminate retries as successes | ordinary Python return values including `None`, `False`, `0`, empty containers | E0 |
| A4 | Operational | fixed backoff without a remaining-budget check can overshoot the deadline and permit a late retry | positive backoff with total scheduling budget | E0 |
| A5 | Architectural | injected clock and sleep functions are sufficient to test retry scheduling deterministically | scheduling/deadline logic only; not cancellation of in-progress calls | E0 |
| A6 | Operational | synchronous retry scheduling cannot guarantee a hard wall-clock cap on an already-running attempt without stronger cancellation machinery | callable execution time itself | E0 |

Neighboring/boundary cases required before broader promotion: zero backoff, exact deadline, max-attempt boundary, falsy success, retryable subclass, nonretryable exception.
