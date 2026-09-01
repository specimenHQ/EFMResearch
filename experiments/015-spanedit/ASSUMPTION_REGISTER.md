# Assumption Register — SpanEdit

Protocol: v0.3

| ID | Class | Assumption | Claim scope | Falsifier / decision effect |
|---|---|---|---|---|
| A1 | Architectural | applying original-coordinate edits left-to-right can shift later targets and produce the wrong result | non-overlapping edits where an earlier replacement changes length | left-to-right mutation still matches independently reconstructed expected text; application-direction concern weakens |
| A2 | Architectural | after validation, right-to-left mutation preserves original coordinates for non-overlapping edits | replacements/deletions/insertions under frozen conflict rules | a valid batch differs from forward streaming reconstruction; reject right-to-left design |
| A3 | Operational | half-open span rules allow adjacent nonempty edits and boundary insertions while rejecting strict interior insertions | controlled boundary fixtures | declared boundary behavior cannot be represented consistently; revise conflict model |
| A4 | Operational | Python `str` slicing uses Unicode code-point indices rather than UTF-8 byte offsets | tested strings containing multibyte code points and combining marks | slices behave according to encoded-byte positions; coordinate authority changes |
| A5 | Operational | multiple insertions at the same original position are ambiguous if declaration order is not semantic authority | two insertions at one position | permutations necessarily produce the same result without an additional ordering rule; duplicate-insertion rejection may be unnecessary |
| A6 | Operational | a forward streaming reconstruction from original segments can independently derive expected output for valid batches | nontrivial valid batches including boundary insertions | streaming oracle requires the same mutation logic or disagrees on valid fixtures; evaluator strategy changes |

Prebuild completeness requirement: A1–A6 must each be tested, durably deferred, or removed from active scope before meaningful implementation begins.

Neighbor cases required before implementation: empty batch, deletion, length-expanding replacement, adjacent spans, insertion at start boundary, insertion at end boundary, insertion strictly inside a span, duplicate insertion position, Unicode multibyte code point, combining mark, and declaration permutation.