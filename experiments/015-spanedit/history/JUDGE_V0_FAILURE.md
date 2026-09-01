# Rejected Judge v0 — SpanEdit

The first adversarial judge was rejected before any E3 result was accepted.

## Failure

The judge's `verify(candidate)` function called known-good fixtures directly. One known-false candidate intentionally rejected all boundary insertions, so it raised `ValueError` on the valid fixture containing an insertion at the end boundary of `[1,3)`.

Instead of interpreting that exception as evidence that the candidate failed a known-good case, judge v0 let the exception escape and aborted the entire judge run.

Observed result: judge process failed before mutant accounting completed.

## Correction

Known-good candidate calls are now wrapped so an exception returns `False` from `verify`. The same protection was added to the declaration-permutation equivalence check.

No application code changed. After the evaluator correction, all 5 known-false editors were rejected and the accepted implementation was accepted.

Classification: evaluator defect discovered during judge hardening. Preserved as research evidence rather than erased.