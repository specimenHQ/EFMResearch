# Experiment Index

This table summarizes experiments whose outcomes have been reviewed in the active non-cyber continuation. Numbering is append-only; preserved historical gaps are not renumbered.

| ID | Experiment | Track | Current result |
|---|---|---|---|
| 001 | Neutral ISO-8601 timestamp sorter | comparison/null | Build-first and EFM both passed the common adversarial suite; EFM added evidence but did not improve delivered correctness on the small bounded task. |
| 002 | SlotLock | EFM-native | Preimplementation evidence constrained the design; integration exposed a false internal-error-as-conflict classification in v0, corrected in v0.1. |
| 003 | MergeSafe | EFM-native | EFM changed parser design and later exposed overgeneralization in its own first equivalence evidence; rejected v0, final 12/12 integration and 7/7 judge mutants rejected. |
| 006 | RetryBudget | EFM-native | Evidence changed deadline/backoff semantics before implementation. Final 10/10 integration; evaluator false rejection corrected; 5/5 false implementations rejected. Accepted at E5. |
| 008 | MoneySplit | exploratory EFM-native / protocol deviation | A1 changed numeric architecture before code, but A2–A6 were tested post-hoc. Useful evidence retained; excluded from clean v0.2 replication credit. |
| 010 | RecordTape | EFM-native | Preimplementation evidence changed record framing twice. Final 11/11 integration, post-green torn-write challenge passed, 5/5 false designs rejected. Accepted at E5 within narrow scope. |
| 011 | QueueGate | EFM-native | Preimplementation evidence changed close/admission architecture. Final 11/11 integration; 200-round post-green race challenge passed; 5/5 false designs rejected. Accepted at E5 within scope. |
| 012 | RowMerge | EFM-native | Four data-reconciliation shortcuts were falsified before implementation. Initial evaluator mistake corrected without application change; final 11/11 integration and 5/5 false designs rejected. E5 within CSV-reconciliation scope. |
| 013 | WallClock | EFM-native | First clean v0.3 run. Direct timezone attachment and fixed UTC 24-hour stepping were rejected before code; prebuild gate 6/6 accounted, evaluator expectations independently checked, final 12/12 integration and 5/5 false designs rejected. Accepted at E5 within tested local-scheduling scope. |

## Protocol markers

- Experiments 001–003: Protocol v0.1.
- Later studies retain the protocol/classification recorded in their own artifacts.
- Protocol v0.3 begins prospectively with experiment 013 and is frozen for experiments 013–015.
- Protocol-deviant runs remain in the history but do not receive clean-replication credit.

## Active boundary

New experiments are restricted to non-cyber software domains. Historical material remains preserved but is not expanded into cybersecurity research.
