# Goal — Experiment 013 WallClock

Build a small standard-library scheduler that resolves a requested local wall-clock time across an inclusive range of local calendar dates in a named IANA timezone.

For every requested local date/time, the result must explicitly classify the wall time as one of:

- **unique** — exactly one real instant exists;
- **ambiguous** — two real instants exist because the local clock repeats;
- **nonexistent** — no real instant exists because the local clock skips forward.

For unique or ambiguous times, return timezone-aware instants without silently changing the requested wall time. Preserve the requested local date/time in the result.

Scope: Python standard library, `zoneinfo`, local calendar scheduling, one named timezone at a time. No recurrence-rule language, distributed scheduling, external calendar APIs, or cybersecurity work.

Protocol: v0.3. Goal frozen before microtests or implementation.
