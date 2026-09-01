# Preimplementation Results — RowMerge

Protocol: v0.2 procedure. Domain: local CSV/data reconciliation only.

## A1 — Identifier representation
**FALSIFIED naive numeric identity.**

Fixture `001` and `1` become the same identifier under integer coercion. The distinct digit strings `9007199254740992` and `9007199254740993` also collapse to the same tested binary-float value.

Decision: identifiers remain opaque strings end-to-end; no numeric coercion or normalization.

## A2 — CSV parser boundary
**PASS at E2 within declared fixtures.**

Python `csv.DictReader` correctly parsed:
- `alpha,beta` from a quoted comma field;
- `He said "hi"` from doubled CSV quotes;
- `line1\nline2` from an embedded newline field;
- CRLF record boundaries in the same fixture.

Decision: standard-library `csv` is sufficient for the tested syntax; no custom parser or dependency added.

## A3 — Duplicate identifiers
**FALSIFIED naive dict overwrite.**

Two rows with ID `001` and different values collapsed to one row when indexed as `{id: row}`; the latter silently replaced the former.

Decision: duplicate IDs are an explicit ambiguity error before reconciliation output is accepted.

## A4 — Blank identifiers
**FALSIFIED naive blank-ID indexing.**

Two blank-ID rows collapsed to one empty-string dictionary key.

Decision: blank/missing IDs are reported as invalid rows and never participate in matching.

## A5 — Deterministic ordering
**FALSIFIED reliance on source insertion order.**

Reversing the same left-side rows changed the order of a naive matched/left-only report.

Decision: output classes and identifiers receive explicit deterministic ordering independent of source row order.

## A6 — Parsed-field versus byte identity
**SCOPE BOUNDARY CONFIRMED.**

LF and CRLF CSV byte streams parsed to the same field values while remaining byte-distinct inputs.

Decision: RowMerge promises preservation of parsed field text, not byte-for-byte CSV serialization identity. Any future byte-preservation requirement would require a different experiment.

## Evidence summary

- A1: E2 falsification → architecture constrained.
- A2: E2 support within tested parser fixtures.
- A3: E2 falsification → duplicate handling required.
- A4: E2 falsification → invalid-row channel required.
- A5: E2 falsification → explicit sorting required.
- A6: E2 scope evidence → byte identity explicitly excluded.

No cybersecurity claim or security testing is part of this experiment.
