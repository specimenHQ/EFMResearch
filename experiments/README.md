# Experiment Index

| ID | Experiment | Track | Current result |
|---|---|---|---|
| 001 | Neutral ISO-8601 timestamp sorter | comparison/null | Both build-first and EFM implementations passed the common adversarial suite; EFM added evidence but did not improve correctness on this small bounded task. |
| 002 | SlotLock | EFM-native | Preimplementation evidence constrained the design; integration testing exposed a false internal-error-as-conflict classification in v0, corrected in v0.1. |
| 003 | MergeSafe | EFM-native | Cross-domain filesystem/data build. A7 changed parser design before implementation; later judge hardening exposed A8 numeric-equivalence overreach and A9 duplicate-key silent rewrite. Rejected v0; final 12/12 integration tests and 7/7 judge mutants rejected. |

Future experiment IDs are append-only. Do not renumber prior studies.
