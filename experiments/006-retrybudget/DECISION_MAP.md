# Decision Map — Initial

1. Clock: wall clock vs monotonic clock.
2. Deadline: per-attempt vs one total retry-scheduling budget.
3. Retry authority: exception class vs return-value truthiness/status.
4. Backoff: fixed sleep vs remaining-budget-clipped sleep.
5. Stop authority: max attempts, deadline, nonretryable exception, or success.
6. Testability: real sleeping only vs injectable clock/sleep boundary.

Architecture is not selected until admitted assumptions are tested.
