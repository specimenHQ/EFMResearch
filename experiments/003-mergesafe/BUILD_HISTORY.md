# Build History — MergeSafe

## v0 — Rejected after first integration / judge hardening

The first implementation was evidence-earned from A1–A7:

- strict rejection of `NaN`/`Infinity`;
- parsed-object rather than raw-text duplicate handling;
- sorted-key JSON serialization;
- deterministic record ordering;
- symlink-aware output/input alias rejection;
- staged temp-file + `fsync` + `os.replace` output commit;
- no third-party dependencies.

Its initial 8-test integration suite passed.

The run was **not** closed at that point because the protocol still required adversarial judge work. Two new dangerous assumptions appeared:

### A8 — numeric equivalence gap

`{"n":1}` and `{"n":1.0}` parse as equal Python JSON values, but v0's `json.dumps`-based canonical strings differed. The same logical record therefore produced a false conflict.

This showed that the original A2 microtest had overfit equivalence to whitespace/key-order variation and had not established numeric equivalence.

### A9 — duplicate object-member loss

Python's default JSON object parser accepts `{"x":1,"x":2}` and silently keeps only the last value. v0 therefore permitted input data to be rewritten at the parse boundary without an explicit decision.

## v0.1 — Current

The smallest coherent correction was:

1. parse JSON numbers losslessly with `decimal.Decimal`;
2. reject duplicate object member names with `object_pairs_hook`;
3. keep explicit rejection of non-standard constants;
4. replace `json.dumps` as the equivalence/canonicalization boundary with a small project-canonical recursive serializer;
5. normalize mathematically equal JSON number spellings (`1`, `1.0`, `1e0`) to one deterministic number representation;
6. keep JSON booleans distinct from numbers;
7. retain the existing staged output and path-safety architecture unchanged.

The project-canonical serializer is an internal deterministic representation for this experiment. It is **not** claimed to implement RFC 8785/JCS.

Diff from rejected v0 to v0.1: **58 added / 8 removed lines** in the implementation.
