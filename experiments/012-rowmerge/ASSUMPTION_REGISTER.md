# Assumption Register — RowMerge

| ID | Class | Assumption | Claim scope | Falsifier / decision effect |
|---|---|---|---|---|
| A1 | Architectural | Treating identifiers as numbers can change identity (for example by removing leading zeros or exceeding exact numeric representation) | digit-looking CSV identifiers | Any fixture where numeric coercion changes distinct textual IDs → keep IDs as opaque strings |
| A2 | Architectural | Python `csv` can correctly parse the required quoting cases | quoted comma, doubled quote, embedded newline, CRLF/LF fixtures | Any required fixture parses incorrectly → stop/reconsider parser or dependency constraint |
| A3 | Operational | Duplicate identifiers make a one-to-one join ambiguous | duplicates within either source | Two rows with same ID but different contents can both plausibly match → duplicates must be surfaced, not auto-selected |
| A4 | Operational | Blank/missing identifiers cannot participate in an exact-ID reconciliation without inventing identity | empty/missing ID column values | Multiple blank-ID rows would collapse into one identity → reject/report invalid rows |
| A5 | Architectural | A deterministic result can be defined independently of source row order | matched/left-only/right-only sets | Permuting either input changes result ordering or classification → explicit deterministic ordering required |
| A6 | Operational | Preserving parsed field text is sufficient for this task; byte-for-byte CSV serialization identity is not required | parsed row field values | A needed requirement depends on original quoting/line-ending bytes → current scope is insufficient and experiment must stop or revise prospectively |

Neighbor/boundary fixtures required before broader promotion: `001` vs `1`, very long digit IDs, quoted comma, embedded newline, escaped quote, duplicate IDs with equal and unequal rows, blank ID, reordered inputs, and unmatched rows on both sides.

All claims are about local CSV/data reconciliation only; no cybersecurity claim is in scope.
