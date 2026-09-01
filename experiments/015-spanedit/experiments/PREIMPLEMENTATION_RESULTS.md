# Preimplementation Results — SpanEdit

Protocol: v0.3

All admitted consequential assumptions A1–A6 were exercised before implementation.

- **A1 FALSIFIED naive left-to-right mutation / E2:** source `abcdef` with edits `(1,2)->WXYZ` and `(4,5)->Q` produced `aWXYQcdef`, changing the later target because the first edit shifted original coordinates. Decision: left-to-right mutation rejected.
- **A2 PASS / E2:** right-to-left mutation produced `aWXYZcdQf`, matching an independent forward streaming reconstruction. Decision: right-to-left remains candidate implementation.
- **A3 PASS / E2:** adjacent nonempty spans and insertions at a nonempty span's start/end boundaries were representable without conflict; an insertion strictly inside `[1,3)` was correctly classified as conflicting. Decision: retain frozen half-open boundary rules.
- **A4 PASS / E2:** Python string `A🙂e\u0301B` had 5 code points but 9 UTF-8 bytes; slices selected the emoji and `e`+combining-mark by Python string positions. Decision: coordinates remain Python `str` indices; no byte/grapheme layer added.
- **A5 CONFIRMED ambiguity / E2:** two insertions at original position 1 produced `aYXbc` versus `aXYbc` under opposite declaration order. Decision: reject multiple insertions at one original position.
- **A6 PASS / E2:** a forward streaming oracle derived `0ABCD!3478?9` for a four-edit fixture; right-to-left application matched it across all 24 declaration permutations. Decision: use the streaming reconstruction as an independent expectation oracle.

## v0.3 prebuild completeness gate

| Assumption | Status before implementation |
|---|---|
| A1 | tested E2 |
| A2 | tested E2 |
| A3 | tested E2 |
| A4 | tested E2 |
| A5 | tested E2 |
| A6 | tested E2 |

Gate result: **PASS — 6/6 admitted consequential assumptions dispositioned before implementation.**
