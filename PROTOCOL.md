# EFM Research Protocol

Version: `0.2 — Claim-scope hardening`  
Effective: `2026-08-31`  
Status: `FROZEN FOR EXPERIMENTS #004–#006`

## Purpose

This protocol defines what counts as an EFM run during the next replication phase. It is versioned so later results cannot silently change the method that produced earlier results.

EFM is not required for every implementation detail. It is admitted when uncertainty could materially change the project, architecture, reliability, safety, cost, or later work.

## 1. Start before meaningful architecture

For an EFM-native project, record the durable goal before selecting implementation architecture beyond what the problem itself requires.

Create:

1. `GOAL.md`
2. `DECISION_MAP.md`
3. `ASSUMPTION_REGISTER.md`

The goal describes the outcome that must survive implementation changes.

## 2. Rank assumptions by consequence

Use these ordinal classes without assigning invented numerical weights:

1. **Existential** — if false, stop or fundamentally change the project.
2. **Architectural** — if false, change implementation direction.
3. **Operational** — if false, reliability, safety, or cost becomes unacceptable.
4. **Optimizing** — if false, the system still works but less efficiently.
5. **Cosmetic** — preference-level impact.

Full EFM microtesting should normally target existential, architectural, and consequential operational assumptions. Optimizing or cosmetic questions require a specific reason for admission.

## 3. Define a falsifiable uncertainty and claim scope

For each admitted assumption, state:

- what is believed;
- what observation would falsify or materially weaken it;
- what decision would change if it is false;
- the smallest boundary at which the claim can credibly be tested;
- the exact **claim scope** the proposed fixture can support.

A passing fixture supports only the invariant it actually exercises. Do not generalize from one representation, equivalence case, failure class, or boundary condition to a broader class without additional evidence.

Do not code a broad implementation merely to discover whether the assumption was valid.

## 4. Run the smallest credible microtest

A microtest must:

- exercise the real boundary when practical;
- declare its fixture/input;
- produce an observable outcome;
- leave enough durable evidence to inspect independently;
- avoid unnecessary framework or application construction.

When a claim depends on equivalence, identity, parsing, classification, routing, or another family of inputs, include a materially different neighboring or boundary case before treating the result as support for the broader family.

A test that merely prints an expected label is not evidence of the underlying behavior.

## 5. Attack the judge

Before relying on an important evaluator, give it one or more deliberately plausible false cases.

At least one important judge attack should be a **near miss**: a case close enough to valid behavior that a weak judge could plausibly accept it, not only an obviously broken case.

Examples include:

- expected labels with missing records;
- correct filenames with wrong contents;
- fabricated success flags;
- duplicated or copied transition history;
- wrong identity/digest/provenance;
- expected phrases without the required causal behavior;
- expected failure labels produced by the wrong underlying failure class.

If the judge accepts a known falsification, stop and improve the judge before interpreting candidate results.

## 6. Record evidence strength

Use the existing ordinal evidence scale:

- **E0 — Claim:** intuition, preference, or unsupported memory.
- **E1 — Observation:** one uncontrolled example.
- **E2 — Controlled microtest:** declared fixture, boundary, and outcome.
- **E3 — Adversarial microtest:** judge rejects known falsifications.
- **E4 — Reproduction:** repeated independently or on another implementation.
- **E5 — Integration evidence:** survives interaction with other proven pieces.
- **E6 — Operational evidence:** survives representative real use.

Do not translate these levels into invented confidence percentages.

## 7. Let evidence constrain implementation

When existential and architectural assumptions have credible evidence, implement the smallest design consistent with that evidence.

Do not add components merely because they are conventional. Record any architecture decision that is explicitly earned or rejected by an experiment.

## 8. Run a thin integration checkpoint

Individually supported mechanisms must be combined early enough to expose interaction failures before the project becomes expensive to change.

Record:

- failures predicted by microtests;
- emergent failures missed by microtests;
- the earliest checkpoint that could have detected each failure.

A first green integration run is a checkpoint, not automatically completion. Before assigning E5, challenge at least one consequential integration-specific failure path that is not merely a replay of the original microtest fixtures.

An E2/E3 component result must not be presented as E5 or E6 evidence.

## 9. Stop rules

Stop testing and decide when:

- remaining uncertainty cannot realistically change the decision;
- expected information gain is lower than test cost;
- existential and architectural assumptions have credible evidence;
- alternatives are operationally equivalent and the simpler one is adequate;
- only representative real use can resolve the next uncertainty.

Return from building to testing when:

- a new dangerous assumption appears;
- the judge accepts a known falsification;
- integration creates an unexplained interaction failure;
- cost, authority, provenance, recovery, or another critical boundary changes.

## 10. Preserve failures and protocol history

Do not delete or rewrite a failed experiment merely because a later design succeeds.

A protocol change must:

1. receive a new version;
2. state which observations motivated it;
3. state whether earlier results remain comparable;
4. take effect only for subsequent experiments unless a rerun is explicitly labeled as such.

## 11. Required per-project output

At minimum, an EFM-native experiment should leave:

- goal;
- decision map;
- assumption register;
- claim scope for important microtests;
- microtest evidence;
- evidence ledger;
- judge attack where applicable;
- implementation or explicit no-build decision;
- integration checkpoint;
- metrics record;
- outcome summary including negative results.

## 12. Replication constraint

Protocol v0.2 applies prospectively beginning with experiment #004. Experiments #001–#003 remain v0.1 studies.

Do not revise v0.2 during experiments #004–#006 merely to improve an outcome. Record proposed changes separately and review them after #006 unless a protocol-integrity defect makes continued use invalid.
