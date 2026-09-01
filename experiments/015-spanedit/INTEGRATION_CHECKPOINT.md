# Integration Checkpoint — SpanEdit

Protocol: v0.3

## Initial integration

- 14 tests run.
- 14 passed.
- 0 failed.
- No application rework required.

Covered: empty batch, expansion, deletion, insertion, adjacent spans, start/end boundary insertions, insertion between adjacent replacements, interior insertion rejection, overlap rejection, same-position insertion ambiguity, invalid bounds, Unicode code-point coordinates, and declaration-order invariance.

## Independent expectation check

Before accepting the nontrivial four-edit expected output, a separately implemented forward streaming reconstruction derived `0ABCD!3478?9`. It does not mutate from right to left and therefore does not reuse the candidate application mechanism.

## Required post-green challenge

A new Unicode source with six edits combined replacement, deletion, start/end boundary insertion, emoji, and combining-mark content. All 720 declaration permutations matched the independent streaming oracle result `Ω<EMOJI>bćFGH?IJ`.

## Evaluator checkpoint

The first adversarial judge was rejected because an exception on a known-good boundary-insertion case escaped the verifier and aborted the run. After correcting the evaluator only, the judge rejected 5/5 known-false editors. Application code was unchanged.

Evidence ceiling: E5 within the frozen in-memory Python-string editing scope.