# Decision Map — Before Code

| Area | Decision that must be earned | Consequence if wrong |
|---|---|---|
| Record identity | What makes two records the same logical record? | Existential: conflicting data can be silently lost |
| Equivalence | How are duplicate records judged equivalent? | Architectural: formatting/key order may create false conflicts |
| Output commit | When does new output replace previous output? | Operational: failed merge can destroy valid state |
| Path identity | Can output name one of the inputs through another path/symlink? | Operational: source may be overwritten |
| Determinism | What ordering/serialization is stable across input order? | Operational: same inputs can yield different artifacts |
| Dependencies | Are external JSON/schema/canonicalization packages necessary? | Optimizing |

CLI wording, colors, progress display, and performance optimization are not admitted to EFM for this build.
