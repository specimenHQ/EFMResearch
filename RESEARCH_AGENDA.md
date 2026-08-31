# Evidence-First Microtesting Research Agenda

Version: `0.1 — Exploratory`  
Status: `OPEN HYPOTHESIS`

> This document is itself an experiment. Its claims must earn authority through
> evidence rather than repetition or preference.

## Working definition

**Evidence-First Microtesting (EFM)** is a development method that resolves
dangerous assumptions through the smallest credible falsifiable experiments,
independently inspects their durable evidence, and attacks the measuring
instrument for false positives before implementation expands.

The broader possibility is **Evidence-First Design**: using this logic across
the entire design spectrum rather than only for isolated technical events.

## Central hypothesis

> EFM produces more decision-changing evidence per minute, token, dollar, and
> unit of implementation complexity than build-first development.

This hypothesis is unproven. One promising content-pipeline case study is not
enough to claim a universal method.

## Scientific loop

```text
Observation
→ uncertainty
→ falsifiable assumption
→ controlled boundary experiment
→ adversarial test of the judge
→ durable evidence
→ confidence update
→ next highest-value uncertainty
```

## Global design loop

```text
Goal
→ decision map
→ assumption map
→ ranked uncertainties
→ microtests
→ evidence ledger
→ confidence updates
→ thin integration checkpoint
→ new interaction uncertainties
→ more microtests
→ earned implementation
```

## Five project artifacts

1. **Goal** — the durable outcome that must survive implementation changes.
2. **Decision map** — choices across product, content, UX, architecture, AI,
   operations, security, cost, and business.
3. **Assumption register** — what must be true for each choice to succeed.
4. **Evidence ledger** — what is supported, by which experiment, at what strength.
5. **Integration checkpoints** — where individually proven pieces must be tested
   together for emergent failure.

## Applying EFM across the design spectrum

| Area | Example assumption | Small credible experiment |
|---|---|---|
| Product | The outcome is valuable | Manually deliver it before automating it |
| Content | A metaphor communicates the intended idea | Blind comparison with representative viewers |
| UX | Editors understand approval state | Paper prototype with one realistic task |
| Architecture | Recovery prevents duplicate action | Real process-kill and receipt test |
| Data | Provenance survives transformation | Transform one record and verify its evidence chain |
| AI | A smaller model meets the quality threshold | Blind comparison on a frozen small fixture |
| Cost | Local processing is cheaper overall | Measure one representative workload end to end |
| Operations | Retry cannot duplicate publication | Idempotency-keyed side-effect test |
| Security | One task cannot read another task's state | Cross-boundary access attempt |
| Portability | A framework can be replaced | Export one workflow and load it without the framework |
| Business | The workflow saves meaningful effort | Operate it manually and measure time and defects |

## Evidence-strength scale

- **E0 — Claim:** intuition, preference, or unsupported memory
- **E1 — Observation:** one uncontrolled example
- **E2 — Controlled microtest:** declared fixture, boundary, and outcome
- **E3 — Adversarial microtest:** judge rejects known falsifications
- **E4 — Reproduction:** repeated independently or on another implementation
- **E5 — Integration evidence:** survives interaction with other proven pieces
- **E6 — Operational evidence:** survives representative real use

EFM must never imply that E3 proves E6.

## Assumption importance

Do not count tests as votes. Rank assumptions by consequence:

- **Existential:** if false, stop or fundamentally change the project
- **Architectural:** if false, change the implementation direction
- **Operational:** if false, reliability, safety, or cost becomes unacceptable
- **Optimizing:** if false, the system still works but less efficiently
- **Cosmetic:** preference-level impact

One unresolved existential assumption outweighs many cosmetic passes.

## Research questions

1. Does EFM reduce time, model usage, code, dependencies, commits, and rework?
2. Does it detect dangerous assumptions earlier than build-first work?
3. Does adversarial judge testing reduce false confidence?
4. How small can a test become before it stops being credible?
5. Can isolated evidence predict integration behavior?
6. Which interaction failures require thin vertical slices?
7. Does EFM work outside deterministic software problems?
8. Can independent investigators reproduce its decisions?
9. Does an evidence ledger prevent repeated investigation?
10. Which confidence notation informs decisions without creating false precision?
11. What stopping rules prevent endless experimentation?
12. Can architecture emerge from an evidence graph without becoming incoherent?

## Initial experiments

### EFM-001 — Build-first versus evidence-first

Assign comparable decisions to two approaches:

- Build-first investigation
- Evidence-first microtesting

Measure time, tokens, dollars, code, dependencies, defects found, rework, and
decision-confidence change.

### EFM-002 — Attack the judge

Create plausible but falsified evidence packages:

- Expected labels with no records
- Copied transition history
- Fabricated success flags or counts
- Missing provenance
- Mismatched identities or digests

Measure how reliably the method rejects them before accepting the candidate.

### EFM-003 — Local evidence versus integration

Prove three mechanisms separately, then combine them in a thin slice. Record:

- Failures predicted by microtests
- Emergent failures missed by microtests
- The earliest point an integration checkpoint would have detected them

### EFM-004 — Cross-domain reproduction

Apply the method to:

- One content-pipeline decision
- One Aleph/control-plane decision
- One UX or content decision
- One model or software-selection decision

Compare evidence quality, cost, and decision usefulness across domains.

## Stopping rules

Stop testing and decide when:

- Remaining uncertainty cannot realistically change the decision.
- Expected information gain is lower than the test cost.
- Existential and architectural assumptions have credible evidence.
- Candidates are operationally equivalent and the simpler one is adequate.
- The next uncertainty can only be resolved through representative real use.

Stop building and return to testing when:

- A new dangerous assumption appears.
- The judge accepts a known falsification.
- Integration produces an unexplained interaction failure.
- Cost, authority, provenance, or recovery boundaries change.

## Failure modes of EFM

- **Weak-judge confidence:** expected labels pass without durable evidence
- **Trivial-test accumulation:** many small passes obscure one critical unknown
- **Local optimization:** isolated components pass but the system interaction fails
- **Fixture overfitting:** candidate logic recognizes examples rather than invariants
- **Self-reporting:** the candidate grades its own behavior
- **False precision:** confidence percentages imply more measurement than exists
- **Endless inquiry:** experiments continue after they can no longer change a decision
- **Premature doctrine:** exploratory principles become rules without reproduction

## Core metric

> **Decision-changing evidence gained per unit of time, cost, and complexity.**

This should be compared with defect escape, rework, and operational outcomes. A
fast test that produces weak or misleading evidence is not efficient.

## Current case-study evidence

The content-pipeline lab has shown that:

- A small real-process crash test produced stronger recovery evidence than a
  larger simulated workflow test.
- An adversarial validator test exposed seven false-positive paths in minutes.
- Strengthening the judge revealed a durable-evidence defect shared by both
  candidates.
- Exact workflow, artifact, version, and digest identity can be tested cheaply.

These results justify further investigation of EFM. They do not yet prove the
global Evidence-First Design hypothesis.

## Deepest open question

> Can a project be designed as an evidence graph, where implementation becomes
> the consequence of sufficiently strong and sufficiently connected evidence?

If so, the primary material of design is not code. It is knowledge about goals,
decisions, assumptions, boundaries, failures, and interactions. Code becomes a
promoted artifact of that knowledge rather than the first place uncertainty is
discovered.
