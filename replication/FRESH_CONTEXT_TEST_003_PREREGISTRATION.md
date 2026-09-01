# Fresh-Context Reconstruction Test 003 — Preregistration

Date prepared: 2026-09-01
Target: Experiment 015 SpanEdit
Purpose: test future-AI transfer of **failure/evaluator provenance**, not only successful architecture reasoning.

## Platform accommodation

The external platform used for prior reconstruction tests reported that it has no Python runtime. Test 003 is therefore **inspection-first and runtime-optional**. No scoring criterion requires code execution. Runnable artifacts remain in the packet for inspection and for use by other future platforms, but inability to execute them is not a defect or deduction.

## Why SpanEdit

DAGPlan tests 001–002 established strong transfer of evidence-earned architecture and retest boundaries. SpanEdit adds a materially different requirement: the handoff must preserve a failed evaluator without confusing it with an application failure.

The critical historical sequence is:

1. A1–A6 prebuild evidence completed before implementation.
2. Evidence-earned application implementation written.
3. Independent expectation check passed.
4. Initial integration passed 14/14 with no application rework.
5. Post-green challenge passed all 720 declaration permutations.
6. Judge v0 failed because an exception from a known-false candidate on a known-good boundary-insertion fixture escaped the verifier.
7. Judge v0 was rejected; no E3 claim accepted from it.
8. Evaluator-only correction converted exceptions on known-good candidate calls/permutation checks into candidate rejection.
9. Application code remained unchanged.
10. Corrected judge rejected 5/5 known-false editors and accepted SpanEdit, earning J1/E3.

## Critical reconstruction requirements

A fresh AI must:
- classify J0 as evaluator defect, not application defect;
- deny E3 credit to J0;
- preserve the failed judge artifact rather than erase it;
- recognize that J1 earns E3 only after correction;
- preserve that application code did not change between J0 and J1;
- distinguish frozen-goal, evidence-earned, incidental, and unproven changes;
- recognize that a forward-streaming candidate would invalidate the independence of the current forward-streaming oracle and therefore require a new independent evaluator strategy.

## Thresholds

- 80+: pass
- 90+: strong pass
- 97+: near-lossless provenance handoff

Any critical provenance error overrides the numeric score.

Packet SHA-256: `bffe09e57978017b90406ebc9ed3808d273a43f69791524e7e8810d4c4379dc2`

The scoring key was frozen separately before external response.
