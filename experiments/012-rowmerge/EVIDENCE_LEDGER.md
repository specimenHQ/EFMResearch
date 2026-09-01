# Evidence Ledger — Experiment 012 RowMerge

| ID | Evidence | Strength | Decision effect |
|---|---|---|---|
| A1 | `001`/`1` collapse under integer coercion; adjacent huge digit strings collapse under tested binary-float coercion | E2 | identifiers remain opaque strings |
| A2 | stdlib `csv.DictReader` preserved quoted comma, escaped quote, embedded newline, and CRLF fixtures | E2 → E5 | use stdlib CSV parser; no custom parser/dependency |
| A3 | naive `{id: row}` indexing silently discarded an earlier duplicate row | E2 → E5 | duplicate IDs are explicit ambiguity errors |
| A4 | two blank-ID rows collapsed to one empty-string key under naive indexing | E2 → E5 | blank/missing IDs are invalid rows, never matches |
| A5 | reversing source rows changed naive insertion-order output | E2 → E5 | matched/unmatched output is explicitly sorted by exact ID text |
| A6 | LF and CRLF byte-distinct CSV inputs produced equal parsed field values | E2 scope evidence | parsed field text is preserved; byte-for-byte serialization identity is not claimed |
| J0 | first post-green evaluator used an incorrect hand-written Unicode order and falsely rejected correct output | E2 observation | evaluator corrected; application code unchanged |
| J1 | 5/5 known-false implementations rejected, including lowercase-normalization near miss; current implementation accepted | E3 | judge accepted |
| I1 | corrected integration 11/11 pass; exact Unicode/case identity post-green challenge passes | E5 | implementation accepted within scoped local CSV reconciliation |

No E6 evidence and no cybersecurity claim.
