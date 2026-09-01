# EFM Preimplementation Results — Experiment 016 Line Mapper

Protocol: v0.3

All admitted consequential assumptions A1–A6 were exercised after the build-first arm was frozen and before the EFM implementation was written.

- **A1 FALSIFIED convenience API / E2:** `str.splitlines(keepends=True)` split U+2028, NEL (`\x85`), vertical tab, and form feed even though the frozen task recognizes only `\n`, `\r`, and `\r\n`. Decision: `splitlines` rejected as segmentation authority.
- **A2 PASS / E2:** an explicit `\r`/`\n` scanner matched a separately implemented regex oracle `\r\n|\r|\n` on fixed boundary fixtures and 500 seeded mixed-Unicode strings. Decision: explicit scanner retained.
- **A3 CONFIRMED / E2:** `splitlines` returned no logical line for empty text and no final empty element for strings ending in `\n`, `\r`, or `\r\n`. The frozen requirements therefore need explicit final-line representation.
- **A4 PASS / E2:** for `a\r\nb`, offset 1 mapped to line 0 end, offset 2 was the invalid CRLF-interior boundary, and offset 3 mapped to line 1 column 0. Decision: retain three-boundary CRLF semantics.
- **A5 PASS / E2:** `A🙂e\u0301B` had 5 Python code points and 9 UTF-8 bytes; Python slices selected by code-point positions. Decision: no byte/grapheme layer.
- **A6 PASS / E2:** the exact-separator regex oracle distinguished the frozen one-line interpretation of `a\u2028b` from the two-line result produced by `splitlines`. Decision: use regex oracle plus round-trip invariants in later evaluation.

## v0.3 prebuild completeness gate

| Assumption | Status before EFM implementation |
|---|---|
| A1 | tested E2 |
| A2 | tested E2 |
| A3 | tested E2 |
| A4 | tested E2 |
| A5 | tested E2 |
| A6 | tested E2 |

Gate result: **PASS — 6/6 admitted consequential assumptions dispositioned before EFM implementation.**

The frozen build-first source was not executed, inspected against these fixtures, or modified during this investigation.