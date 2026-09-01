# EFM Blind Reproduction Start Packet

Give this file to an investigator/model that has **not** read the EFM experiment history. Do not provide existing experiment outcomes or implementations before the reproduction is complete.

## Research boundary

Run one prospective **non-cyber** software experiment using Evidence-First Microtesting.

The purpose is not to prove EFM succeeds. Preserve a null, failure, stop decision, evaluator defect, or protocol deviation exactly as observed.

## Method

### 1. Freeze the goal before architecture

Write a durable task goal and explicit scope exclusions before meaningful implementation.

Choose or receive a task independently. It should contain at least one uncertainty whose failure could materially change architecture, reliability, cost, or downstream work. Avoid trivial tasks selected only because the solution is obvious.

### 2. Map decisions and assumptions

Before implementation, write:

- decisions that evidence could change;
- consequential assumptions;
- each assumption's consequence class: existential, architectural, operational, optimizing, or cosmetic;
- what would falsify it;
- what decision would change;
- the exact scope supported by the proposed test.

Do not invent numeric assumption weights.

### 3. Pass the prebuild completeness gate

Before meaningful implementation, every admitted existential, architectural, and consequential operational assumption must be one of:

- tested with durable evidence;
- explicitly deferred with a durable reason and excluded from the current claim;
- removed from active scope.

If a consequential assumption is silently carried into implementation untested, preserve the run but mark it protocol-deviant rather than repairing its history afterward.

### 4. Use the smallest credible microtests

Test the real boundary when practical. Each important test should have declared input/fixture, observable outcome, and inspectable evidence.

A passing fixture supports only what it actually exercised. For claims about equivalence, identity, parsing, classification, routing, boundaries, or families of inputs, include a materially different neighboring case before generalizing.

### 5. Let evidence constrain implementation

Implement the smallest design consistent with the evidence. Do not add components merely because they are conventional.

Record when evidence changes or rejects an architecture decision.

### 6. Check the evaluator before trusting it

For important nontrivial expected values, independently derive or check the expectation using a different calculation, oracle, invariant, representation, or obviously known-good neighboring case.

Attack the evaluator with deliberately false and near-miss implementations/cases before trusting candidate results.

If the evaluator accepts a known falsification or an important expected value fails its independent check, fix or reject the evaluator before interpreting application results.

### 7. Integrate, then challenge again

Run a thin integration checkpoint. A first green run is not automatically completion.

Before assigning integration evidence, run at least one consequential post-green challenge that is not merely a replay of the prebuild fixtures.

### 8. Evidence levels

Use only these ordinal labels:

- E0 — Claim
- E1 — Observation
- E2 — Controlled microtest
- E3 — Adversarial microtest / judge rejects known falsifications
- E4 — Independent reproduction
- E5 — Integration evidence
- E6 — Representative operational evidence

Do not convert them into percentages or a universal score.

This reproduction does not automatically earn E4. A separate reviewer must determine whether the investigator/task/evidence were sufficiently independent and reproducible.

## Required artifacts

Create and preserve:

- `GOAL.md`
- `DECISION_MAP.md`
- `ASSUMPTION_REGISTER.md`
- prebuild microtests/fixtures and raw results
- prebuild completeness record
- implementation or explicit stop/no-build decision
- independent expectation/oracle checks
- integration tests/results
- adversarial judge/results
- post-green challenge/results
- `EVIDENCE_LEDGER.md`
- `METRICS.md`
- `RUN_LOG.md`
- `OUTCOME.md`

## Prospective measurements

Record when available rather than reconstructing later:

- active work time;
- time to first meaningful implementation;
- assumptions and consequence classes;
- microtest count;
- implementation and evaluator logical LOC;
- dependencies;
- architecture decisions changed by evidence;
- defects found prebuild/integration/post-green;
- rework/discarded implementation;
- evaluator defects;
- judge false cases attempted/rejected/accepted;
- token/dollar cost only if independently measurable.

Never invent missing measurements.

## Final instruction

Report what happened, not what would make EFM look successful. Do not read the existing EFM experiment outcomes until your run and artifacts are frozen.