# Decision Map — Experiment 013 WallClock

| Decision | Depends on | If falsified |
|---|---|---|
| Use direct `datetime(..., tzinfo=ZoneInfo(...))` construction as authoritative validation | A1 | add an explicit validation/classification step instead of trusting attachment |
| Represent repeated local times with `fold=0` and `fold=1` | A2 | choose another stdlib representation or stop if ambiguity cannot be represented faithfully |
| Classify unique/ambiguous/nonexistent wall times by UTC round-trip behavior | A3 | reject the proposed classifier and search for another observable invariant |
| Iterate by local calendar dates, not by adding 24 hours to UTC instants | A4 | if 24-hour UTC stepping preserves the intended local wall time, simpler instant iteration may be sufficient |
| Treat the two ambiguous folds as distinct only when their UTC instants differ | A5 | revise ambiguity criterion to avoid duplicate pseudo-occurrences |
| Use system `zoneinfo` data without adding a dependency | A6 | if the required named timezone is unavailable, record environment limitation rather than silently substituting fixed offsets |

Implementation does not begin until the Protocol v0.3 prebuild completeness gate records a disposition for A1–A6.
