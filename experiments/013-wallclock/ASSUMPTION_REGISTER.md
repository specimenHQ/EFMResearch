# Assumption Register — Experiment 013 WallClock

Protocol: v0.3

| ID | Class | Assumption | Falsifier | Claim scope |
|---|---|---|---|---|
| A1 | Architectural | attaching `ZoneInfo` directly to a nonexistent local wall time does not itself provide reliable validity classification | direct construction clearly rejects or uniquely classifies a spring-forward gap | tested `America/New_York` spring-forward wall time |
| A2 | Architectural | `fold=0` and `fold=1` can represent the two real instants of a repeated fall-back wall time | both folds resolve to the same instant for a known repeated wall time | tested `America/New_York` fall-back wall time |
| A3 | Existential | local→UTC→local round-trip behavior can distinguish unique, ambiguous, and nonexistent wall times | any of the three classes cannot be distinguished on controlled fixtures | controlled unique/gap/fold fixtures in one IANA zone |
| A4 | Operational | stepping UTC instants by exactly 24 hours does not preserve a fixed local wall-clock schedule across DST transitions | 24-hour UTC stepping preserves the requested local clock through both tested transitions | daily local schedules crossing tested DST transitions |
| A5 | Operational | a wall time is ambiguous only when both folds round-trip to the requested wall time and map to different UTC instants | criterion misclassifies a controlled unique, gap, or fold case | controlled fixtures in `America/New_York` |
| A6 | Operational | the runtime can load `America/New_York` through stdlib `zoneinfo` | `ZoneInfoNotFoundError` | current experiment runtime only |

Neighbor cases required before broader support: ordinary winter time, ordinary summer time, spring-forward gap, fall-back repeated time, and dates immediately before/after each transition.

No implementation begins until A1–A6 are dispositioned by the v0.3 prebuild completeness gate.
