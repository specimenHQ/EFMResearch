# Decision Map — SpanEdit

Protocol: v0.3

## Decisions that evidence can change

1. **Application direction**
   - Candidate: validate against original coordinates, then mutate from right to left.
   - Alternative: construct the result in one forward streaming pass from original segments.
   - Risk: left-to-right mutation shifts coordinates for later edits.

2. **Conflict model**
   - Nonempty edited spans may touch but not overlap.
   - Insertions may sit at nonempty-span boundaries but not strictly inside them.
   - Multiple insertions at one original position are rejected because declaration order is not semantic authority.

3. **Same-boundary ordering**
   - Candidate right-to-left rule: when an insertion shares the start of a nonempty edit, apply the nonempty edit first and the insertion second so the insertion appears before the replacement in final text.
   - An insertion at a nonempty edit's end is applied first by descending coordinate, so it appears after the replacement.

4. **Coordinate authority**
   - Python Unicode string indexing is the declared coordinate system.
   - No byte-offset or grapheme-cluster normalization is introduced.

5. **Evaluator independence**
   - A forward streaming reconstruction from original source segments is a candidate independent oracle for nontrivial expectations because it does not reuse right-to-left mutation.

No implementation is accepted before all admitted consequential assumptions pass the v0.3 prebuild completeness gate.