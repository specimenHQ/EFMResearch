# Future-AI Handoff — SpanEdit

Handoff standard: v0.1
EFM protocol used for experiment: v0.3

## Frozen goal

Apply a finite batch of edits to one Python Unicode string where every edit coordinate refers to the original, unmodified source. Coordinates are zero-based half-open Python `str` indices `[start,end)`. Declaration order must not change the result.

Frozen semantic requirements include:
- replacements, deletions, and zero-length insertions are supported;
- invalid spans are rejected;
- overlapping nonempty spans are rejected;
- an insertion strictly inside a nonempty edited span is rejected;
- insertions at a nonempty span's start/end boundary are allowed;
- multiple insertions at the same original position are rejected as ambiguous;
- adjacent nonempty spans are allowed;
- task coordinates are Python string code-point indices, not UTF-8 byte offsets or grapheme-cluster indices.

Out of scope: rich text, grapheme segmentation, collaborative editing, persistence, diff generation, and cybersecurity.

## Evidence-earned constraints

- Do not apply original-coordinate edits left-to-right when an earlier edit can change length — A1 directly falsified that authority.
- Right-to-left application is supported within the frozen conflict rules because it matched an independently implemented forward-streaming reconstruction — A2/A6.
- Preserve the frozen half-open conflict model for adjacent spans, boundary insertions, and strict interior insertions — A3.
- Preserve Python `str` code-point indexing unless the coordinate goal itself is changed — A4.
- Reject multiple insertions at one original position while declaration order remains non-semantic — A5.
- Important nontrivial expected output should remain independently checkable by a strategy that does not reuse the candidate's right-to-left mutation logic — A6/X1.

## Evaluator provenance — do not erase

Judge v0 is **rejected evidence machinery**, not an application failure.

Judge v0 called known-good fixtures directly. A deliberately false candidate that rejected valid boundary insertions raised on a known-good fixture; the exception escaped `verify` and aborted the judge run before mutant accounting completed. No E3 claim was accepted from that judge.

The correction was evaluator-only: known-good candidate calls and declaration-permutation comparisons were wrapped so an exception means the candidate is rejected (`False`) rather than crashing the judge. Application code did not change. Corrected judge J1 rejected 5/5 known-false editors and accepted SpanEdit.

A future AI must preserve this distinction:
- `J0`: evaluator defect; rejected judge; no E3;
- `J1`: corrected adversarial evaluator; E3;
- application implementation unchanged between J0 and J1.

## Incidental implementation choices

The current exception names/messages, local variable names, module layout, pairwise-validation loop structure, exact internal container types, and use of repeated string slicing are not individually evidence-earned requirements unless a future external interface makes them part of the goal.

The evidence supports behavior and coordinate/conflict semantics, not every line of the present implementation.

## Unproven alternatives

A forward-streaming implementation is not falsified; in fact, a streaming reconstruction was used as an independent oracle. Replacing right-to-left mutation with a streaming implementation could be valid, but the oracle can no longer serve as an independent evaluator if candidate and oracle become the same algorithm. A new independent oracle/invariant must then be earned before evaluator authority is restored.

Similarly, a byte-offset or grapheme-cluster coordinate system is not 'wrong' in general; it conflicts with the current frozen goal. Adopting one requires revising/freezeing the goal first, then new microtests and expectations.

## Future-change map

- Right-to-left candidate → forward-streaming candidate: **unproven/evidence independence changes**. Re-run behavior tests and replace the streaming oracle with an independent authority.
- Python code-point indices → UTF-8 byte offsets: **goal conflict/new coordinate semantics**. Revise/freeze goal, then microtest Unicode boundaries.
- Allow same-position insertions by declaration order: **goal conflict** because declaration order is currently non-semantic; revise/freeze goal, then microtest ordering semantics.
- Reject all boundary insertions: **goal + evidence conflict**; A3 and judge known-good fixtures establish boundary insertions as valid.
- Allow strict interior insertions: **goal + evidence conflict** under the frozen conflict model.
- Rename exception classes: generally incidental unless exception identity is promoted into a public contract.

## Retest triggers

Re-enter EFM before consequential continuation when:
- the coordinate system changes;
- the conflict model changes;
- declaration order becomes semantic;
- a different application algorithm invalidates evaluator independence;
- edit representation changes enough that original-coordinate simultaneity is uncertain;
- the project expands into grapheme-aware, collaborative, persistent, or other previously excluded behavior.

## Evidence ceiling

A1–A6/X1: E2 within declared fixtures and scope.
J0: evaluator defect, no E3.
J1: E3 after corrected judge rejects 5/5 known-false editors.
I1/I2: E5 within finite in-memory Python-string editing scope.
No E6, universal correctness, optimality, superiority, grapheme-cluster, collaborative-editing, or cybersecurity claim.
