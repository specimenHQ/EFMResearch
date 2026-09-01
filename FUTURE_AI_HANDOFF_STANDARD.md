# Future-AI Handoff Standard

Version: `0.1`  
Purpose: preserve EFM evidence so a future AI session can reconstruct, rerun, and safely extend a build without access to the original conversation.

This is an **artifact standard**, not a change to EFM Protocol v0.3. Protocol v0.3 governs how evidence is earned. This standard governs how earned evidence is packaged for future AI use.

## Core transfer test

A handoff is adequate only if a fresh AI can determine, from durable artifacts alone:

1. what was being built;
2. which assumptions were consequential;
3. what exact experiments exercised those assumptions;
4. what happened in those experiments;
5. which architectural decisions were earned by that evidence;
6. which implementation choices are incidental rather than evidence-earned;
7. what the evidence does **not** establish;
8. what must be retested if a future build changes a consequential decision.

A summary that merely states the final architecture is insufficient.

## Required handoff layers

### 1. Goal and claim boundary

Include the frozen goal and explicit exclusions. A future AI must be able to distinguish a proposed feature extension from a change that violates the original goal.

### 2. Decision map

Record the decisions evidence could change, including alternatives that were considered but not necessarily falsified.

### 3. Assumption register

For every admitted consequential assumption preserve:

- ID and consequence class;
- belief being tested;
- falsifier;
- decision effect;
- exact claim scope.

### 4. Runnable prebuild evidence

Preserve the actual microtest code or fixtures, not only prose summaries of the result. Include raw/pass-fail output when available.

A future AI should not need to reconstruct the original fixture from a sentence such as “duplicate IDs failed.”

### 5. Prebuild completeness record

Preserve which assumptions were tested, deferred, or removed before implementation.

### 6. Evidence-earned constraint map

Create an explicit table separating:

- **Evidence-earned constraint** — changing this invalidates or bypasses existing evidence;
- **Frozen-goal constraint** — changing this changes the project goal and requires a new goal/scope decision;
- **Incidental implementation choice** — may be changed without contradicting current evidence, provided required behavior is preserved;
- **Unproven alternative** — not falsified, but existing evidence does not automatically transfer.

For every evidence-earned constraint state the evidence IDs that support it and the minimum retest required if changed.

### 7. Runnable implementation

Preserve the accepted implementation or explicit stop/no-build decision.

### 8. Runnable expectation/oracle checks

If an important expected result was independently checked, preserve the actual alternate oracle/calculation, not only the sentence that it passed.

### 9. Runnable integration suite

Preserve the complete test/evaluation code and result summary. A future AI must be able to see which cases produced an E5 claim.

### 10. Runnable adversarial judge

Preserve:

- evaluator/verifier code;
- known-false and near-miss candidates;
- what each mutant is intended to falsify;
- judge result.

A statement such as “5/5 mutants rejected” without the mutants is insufficient for durable transfer.

### 11. Runnable post-green challenge

Preserve the challenge fixture, alternate oracle/invariant, and raw result.

### 12. Evidence ledger

Map assumption/evidence IDs to evidence level and decision consequence. Never translate E0–E6 into confidence percentages.

### 13. Run log and outcome

Preserve chronology, evaluator failures, implementation failures, null findings, protocol deviations, evidence ceiling, and explicit nonclaims.

## Required future-change map

Each handoff should include a compact table with columns:

| Proposed future change | Classification | Existing evidence affected | Minimum action before adoption |
|---|---|---|---|

Classification should be one of:

- `goal conflict`
- `evidence conflict`
- `unproven / evidence does not transfer`
- `incidental / evidence-preserving`

This distinction is central. EFM must not turn evidence-earned architecture into dogma. A new architecture may be valid even when it is not supported by the old evidence; in that case the correct action is to re-enter microtesting and earn new evidence.

## Fresh-context acceptance test

Before relying on a handoff for a long-lived project, a fresh AI may be given only the handoff package and asked to:

1. reconstruct the goal and scope;
2. reconstruct assumption → experiment → observation → decision chains;
3. classify evidence strength without overclaiming;
4. identify evidence-earned versus incidental choices;
5. analyze proposed changes as conflict / unproven / incidental;
6. name EFM re-entry points;
7. state what it would rerun before changing architecture;
8. identify missing artifacts that would prevent reproducibility.

The test is evidence about **handoff durability**, not E4 methodology independence.

## Origin of this standard

Fresh-Context Reconstruction Test 001 used a reduced DAGPlan packet on another AI platform. The external reconstruction strongly recovered the goal, evidence-earned architecture, evidence levels, and the crucial distinction between contradicted changes and an unproven DFS alternative. It also identified that the reduced packet omitted exact microtest fixtures, integration tests, oracle implementation, and adversarial judge details even though those artifacts existed in the research repository.

The lesson was therefore not “write more prose.” It was: **package the runnable evidence with the reasoning.**
