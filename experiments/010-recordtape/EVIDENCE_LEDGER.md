# Evidence Ledger — Experiment 010 RecordTape

| ID | Result | Strength | Decision effect |
|---|---|---|---|
| A1 | length-only framing accepted tested payload bit flip | E2 | integrity field required |
| A2 | CRC-only framing lost checksum location on tested 5→13 length mutation; redundant `(length, inverse)` + CRC passed corrective probes | E2 | architecture changed before build |
| A3 | scoped torn header/payload/checksum cases distinguished from complete checksum corruption | E2 → E5 | recovery may truncate torn tail only |
| A4 | 3-byte partial writes reconstructed exact record through write-all loop | E2 → E5 | bounded write loop retained |
| A5 | two valid records + torn third recovered exactly first two across all tested cut points | E2 → E5 | truncate to last verified offset |
| A6 | oversized valid header rejected before payload read | E2 → E5 | fixed maximum retained |
| J1 | 5/5 known-false designs rejected; accepted implementation accepted | E3 | evaluator accepted |
| I1 | 11/11 integration tests plus exhaustive tested torn-tail cut points pass | E5 | implementation accepted |

No E6, collision-resistance, concurrent-writer, storage-device, or power-loss durability claim.
