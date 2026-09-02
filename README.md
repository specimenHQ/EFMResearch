# Evidence-First Microtesting (EFM)

**Status:** exploratory research repository  
**Current protocol:** `0.3 — Prebuild completeness and evaluator integrity`  
**Effective:** 2026-08-31  
**Active research boundary:** non-cyber domains

Evidence-First Microtesting (EFM) is being investigated as a way to resolve consequential assumptions with the smallest credible falsifiable action, preserve what actually happened, and let evidence constrain what gets built next.

This repository preserves the research history. It is intentionally not a claim that EFM is already a proven methodology.

## Research tracks

1. **EFM-native development** — begin with goal, decisions, assumptions, and evidence before meaningful architecture is committed.
2. **Prebugging** — use the method to search for latent defects and false confidence in existing software.
3. **Comparative studies** — compare EFM with ordinary development under frozen requirements and common evaluation.
4. **Negative/null cases** — retain cases where EFM adds cost without changing the result.
5. **Future-AI handoff durability** — test whether a fresh AI session can reconstruct and safely extend evidence-earned work without the original conversation.
6. **Field-use continuity** — use EFM prospectively inside real projects and preserve observations, decisions, unresolved questions, and handoff state as work evolves.

## Protocol history

- `v0.1` governed experiments 001–003.
- `v0.2` added claim-scope hardening and post-green integration challenges.
- `v0.3` began with experiment 013 and added a prebuild completeness gate plus independent checking of nontrivial evaluator expectations.
- `PROTOCOL_REVIEW_AFTER_012.md` records the evidence that motivated v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` reviews three clean v0.3 runs and retains the protocol unchanged.

Earlier experiments keep their original classifications. Protocol changes are prospective rather than retroactive.

`FUTURE_AI_HANDOFF_STANDARD.md` is separate from the protocol: v0.3 governs how controlled evidence is earned; the handoff standard governs how fuller runnable evidence is packaged for later AI sessions.

`CONTINUITY_STANDARD.md` is a lighter operational layer for ongoing field use. It does not replace either document.

## Current evidence pattern

The repository contains a mixed pattern rather than a simple success story:

- multiple EFM-native runs changed architecture before implementation;
- some runs exposed implementation defects, overgeneralized microtests, or evaluator defects;
- controlled comparisons 001 and 016 produced null delivered-correctness results: EFM generated more preimplementation evidence, but the ordinary build-first arm independently delivered an equally correct first implementation;
- protocol-deviant runs remain preserved rather than being promoted to clean replication evidence;
- evaluator failures are preserved separately from candidate failures;
- fresh-context handoff tests recovered project goal, evidence boundaries, architecture reasoning, change-impact logic, and evaluator provenance across new AI contexts/platforms.

No E0–E6 level is converted into a confidence percentage, and no universal EFM score is used.

## Current interpretation

The evidence supports a scope claim more strongly than a universal development claim. EFM appears most defensible when a consequential assumption is genuinely uncertain and can alter architecture, reliability, cost, or expensive downstream work. Controlled null results also show that producing more evidence is not itself enough; on bounded tasks, a careful ordinary implementation may reach the same correct design with less process.

The next practical phase is increasingly longitudinal and real-world. A microtest remains useful when isolation matters, but EFM is not being treated as something that must be proved only through an expanding laboratory program. A bounded real-world event can also become evidence when the question, observation, provenance, and claim boundary are preserved.

The dominant scientific limitations remain. The studies are still largely same-investigator/model and investigator-designed. The repository has no independent E4 methodology reproduction and no representative operational E6 evidence.

## Continuity layer

The default field-use record now has five files:

- `CURRENT_STATE.md` — replaceable snapshot of what is true and active now;
- `EVIDENCE_LEDGER.md` — append-only observations and evidence boundaries;
- `DECISIONS.md` — append-only consequential decisions tied to evidence IDs;
- `OPEN_QUESTIONS.md` — unresolved uncertainties whose status changes but whose history is not deleted;
- `HANDOFF.md` — compact reconstruction map for a fresh AI or collaborator.

The anti-corruption rule is simple: evidence and decisions are history; current state and handoff are caches. Corrections append rather than silently rewriting prior evidence.

Reusable versions live under `templates/continuity/`.

## Repository map

- `CURRENT_STATE.md` — current working snapshot.
- `EVIDENCE_LEDGER.md` — durable root evidence record.
- `DECISIONS.md` — durable root decision record.
- `OPEN_QUESTIONS.md` — unresolved/closed continuity questions.
- `HANDOFF.md` — fresh-context reconstruction map.
- `CONTINUITY_STANDARD.md` — minimal continuity/storage rules for ongoing field use.
- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — controlled EFM method; v0.3 retained unchanged after experiment 015.
- `PROTOCOL_REVIEW_AFTER_012.md` — evidence-based review leading to v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` — review retaining v0.3 unchanged.
- `FUTURE_AI_HANDOFF_STANDARD.md` — fuller artifact-packaging standard for future AI continuity/reproducibility.
- `METRICS.md` — descriptive measurements collected across studies.
- `experiments/` — append-only experiment history.
- `templates/continuity/` — minimal field-use continuity templates.
- `templates/FUTURE_AI_HANDOFF.md` — fuller future-AI handoff template.
- `handoff_tests/` and `reconstruction/` — fresh-context durability evidence.
- `results/INTERIM_SYNTHESIS_AFTER_016.md` — controlled-study synthesis and limitations.
- `replication/` — independent-reproduction materials.

## Active continuation

Current work remains non-cyber. Controlled experiment history is preserved, but the immediate research direction is continuity-first field use.

EFM is now being used prospectively during real work, including Shopify-related store/product decisions. The near-term question is whether the five-file continuity format preserves useful state and provenance without becoming burdensome enough that humans or AI agents stop maintaining it. See `Q-20260902-001`.

Until independent or representative operational evidence exists, no E4 methodology, E6 operational, universal superiority, or statistical-significance claim is warranted.
