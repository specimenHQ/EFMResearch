# Goal — RetryBudget

Provide a small synchronous Python retry utility that retries only configured exception classes, preserves successful values including falsy values, obeys a maximum-attempt limit, and never starts a new retry after a total retry-scheduling deadline.

Scope: the deadline governs whether another attempt may start and how long backoff may sleep. It does **not** promise to interrupt an attempt already executing. No background threads, processes, or third-party dependencies are required unless evidence shows they are necessary.
