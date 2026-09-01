# Fresh-Context Reconstruction Test 001 — DAGPlan

Status: preregistered / awaiting isolated fresh-chat execution

## Research question

Can a future AI conversation with no access to the original EFM discussion reconstruct the meaning of a completed EFM evidence package well enough to continue or modify the build without treating evidence-earned decisions as arbitrary?

This is **not** a test of independent scientific reproduction of EFM. It is a test of durable AI-to-AI decision transfer.

## Source experiment

Experiment 014 — DAGPlan.

Selected because it contains:
- a clear frozen goal and scope;
- six consequential prebuild assumptions;
- both confirmed hazards and a directly falsified staging approach;
- evidence-earned architectural/validation decisions;
- E2, E3, and E5 evidence with an explicit E6 boundary;
- at least one plausible future architecture change (DFS) that is not disproven but would require re-earning evidence.

## Blind packet

The blind packet contains only these experiment artifacts plus the reconstruction prompt:
- `GOAL.md`
- `DECISION_MAP.md`
- `ASSUMPTION_REGISTER.md`
- `PREIMPLEMENTATION_RESULTS.md`
- `EVIDENCE_LEDGER.md`
- `OUTCOME.md`
- `src/dagplan.py`
- `BLIND_PROMPT.md`

The fresh chat must be instructed not to browse the web or search the repository. It must use only the packet.

Packet SHA-256 recorded at creation:
`dc5b5f7884d1980d4755e9e6458df73590d6983fad605b9c3f315c8270d3640a`

## Questions under test

The fresh agent must reconstruct:
1. goal and claim boundary;
2. dangerous assumptions and their observed falsification/support;
3. evidence-earned architecture versus incidental implementation detail;
4. E2/E3/E5 evidence and prohibited overclaims;
5. impact/retest requirements for four proposed future changes;
6. credible EFM re-entry points;
7. confidence/claim discipline;
8. whether the artifacts are sufficient for future continuation and what is missing.

## Critical discrimination cases

The fresh agent must distinguish between:
- changes that violate the frozen goal (for example silently inventing unknown tasks or silently deduplicating repeated dependency declarations), and
- changes that are not disproven but fall outside current evidence (for example replacing Kahn staging with a DFS-based implementation).

It must also identify frozen-frontier staging as evidence-earned rather than arbitrary.

## Evaluation

A separate scoring key exists outside the blind packet. Maximum score: 100. Preliminary durable-reconstruction threshold: 80, with critical-failure overrides for severe evidence-scope errors.

A passing result would be preliminary evidence that EFM artifacts can transfer decision meaning across AI conversation boundaries. A failure should lead to artifact-format improvement rather than retroactive reinterpretation of DAGPlan's application evidence.
