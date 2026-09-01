# Decision Map — RowMerge

## D1 — Identifier representation
If text identifiers with leading zeros or large digit strings are changed by numeric coercion, identifiers remain opaque strings end-to-end. Otherwise no extra normalization is added.

## D2 — CSV parser boundary
If the Python standard-library CSV parser correctly preserves the required quoted commas, quotes, and embedded newlines in controlled fixtures, use it directly. Otherwise stop and reconsider the task or dependency constraint.

## D3 — Duplicate identifiers
If duplicate identifiers make one-to-one reconciliation ambiguous, reject/report the ambiguity before producing matched output. Do not select first/last row implicitly.

## D4 — Ordering
If input order cannot provide a deterministic cross-file result independent of source ordering, define output ordering explicitly by exact identifier text and result class.

## D5 — Missing identifiers
If blank/missing identifiers cannot be distinguished safely from real identifiers, report them as invalid rows rather than joining them.

## D6 — Implementation boundary
Only build after the admitted architectural/operational assumptions are microtested. Keep the implementation local, stdlib-only, and limited to CSV reconciliation.
