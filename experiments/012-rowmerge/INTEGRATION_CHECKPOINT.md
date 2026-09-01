# Integration Checkpoint — RowMerge

## First integrated run

The first run executed 11 tests. Ten passed. One failed in the post-green exact-identity challenge.

Investigation showed the implementation had produced the correct deterministic Python string ordering. The hand-written expected order in the evaluator was wrong. This was a **false rejection by the measuring instrument**, not an application defect.

The evaluator was corrected; application code was not changed.

## Final integrated run

- 11/11 integration tests pass.
- Required quoted CSV syntax passes.
- Numeric-looking identifiers remain opaque text.
- Duplicate IDs are explicit ambiguity errors.
- Blank IDs are separated as invalid rows.
- Result ordering is independent of source row ordering.
- Matched/unmatched rows preserve parsed field text.

## Post-green challenge

A non-replayed neighboring identity case was added after the main suite: composed `é` versus decomposed `e + combining acute`, plus `A` versus `a`. The implementation kept all four exact textual identities distinct and ordered deterministically.

## Evidence level

Implementation evidence reaches E5 for the tested local CSV-reconciliation scope. No E6 claim is made.

No cybersecurity behavior or claim is part of this checkpoint.
