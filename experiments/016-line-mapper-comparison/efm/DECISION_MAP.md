# EFM Decision Map — Experiment 016 Line Mapper

Protocol: v0.3

## Decisions evidence can change

1. **Line segmentation authority**
   - Candidate A: Python `str.splitlines(keepends=True)`.
   - Candidate B: explicit scan limited to `\r`, `\n`, and `\r\n`.
   - Risk: convenience API may recognize separators outside the frozen specification or differ on empty/trailing-line behavior.

2. **Stored representation**
   - Candidate: per logical line store `(content_start, content_end, separator_end)` in original code-point offsets.
   - This representation should support both mapping directions without copying text.

3. **CRLF offset semantics**
   - Content-end boundary before `\r` is valid for the preceding line.
   - Boundary between `\r` and `\n` is invalid.
   - Boundary after `\n` is valid as the next line's column zero.

4. **Coordinate unit**
   - Python string/code-point offsets only; no encoded-byte or grapheme layer.

5. **Evaluator independence**
   - Candidate implementation may use an explicit scanner; independent expectations should use a separately derived separator oracle, such as regex matching of exactly `\r\n|\r|\n`, plus direct round-trip invariants.

No EFM implementation is accepted before the v0.3 prebuild completeness gate passes.