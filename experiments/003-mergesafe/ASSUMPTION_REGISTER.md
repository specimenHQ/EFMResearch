# Assumption Register — Initial State

| ID | Importance | Assumption | Falsifier | Decision if false | Initial evidence |
|---|---|---|---|---|---|
| A1 | Existential | Raw JSON text is not a safe equivalence test because key ordering/whitespace may differ while parsed values are equal | Two unequal JSON strings parse to equal objects | Compare parsed values/canonical form instead | E0 |
| A2 | Architectural | A deterministic canonical representation can be produced with Python stdlib JSON using sorted keys and fixed separators | Equivalent objects serialize differently under the chosen settings | Need another canonicalization rule/library | E0 |
| A3 | Operational | Writing a temporary file in the output directory and replacing only after successful completion leaves an existing output unchanged when failure occurs before replace | Injected pre-replace failure changes old output | Need different commit protocol | E0 |
| A4 | Operational | Filesystem identity can detect an output path that aliases an existing input through a symlink | Symlink alias is not recognized as same file | Need stronger path/identity checks | E0 |
| A5 | Operational | Sorting accepted records by `id` plus canonical JSON serialization makes output independent of input file order | Reordered inputs produce different bytes | Need stronger deterministic ordering | E0 |
| A6 | Optimizing | Python stdlib is sufficient for parsing, canonical serialization, temp-file commit, and path identity | Required boundary cannot be exercised without external package | Admit minimal dependency | E0 |
| A7 | Operational | Python default JSON parsing rejects non-standard numeric constants such as `NaN`/`Infinity` | Default parser accepts one | Add an explicit strict-JSON parse boundary | E0 — discovered during implementation planning |

Stopping rule: after all admitted assumptions are credibly tested, implement the smallest design those results justify. Return to testing if integration exposes a new dangerous assumption.

## Assumptions discovered during integration/judge hardening

| ID | Importance | Assumption | Falsifier | Decision if false | Initial evidence |
|---|---|---|---|---|---|
| A8 | Architectural | The chosen canonical representation preserves intended value equivalence across valid JSON number spellings | Parsed-equal numeric records such as `1` and `1.0` canonicalize differently | Replace serializer/number parsing before accepting duplicate equivalence | E0 — discovered after first integration pass |
| A9 | Operational | The parser does not silently discard duplicate object member names | A record with the same object key twice is accepted with last-write-wins behavior | Reject duplicate member names at parse boundary | E0 — discovered during judge hardening |
