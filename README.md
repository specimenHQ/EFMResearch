# Evidence-First Microtesting (EFM)

**Status:** exploratory research repository  
**Current protocol:** `0.3 — Prebuild completeness and evaluator integrity`  
**Effective:** 2026-08-31  
**Active research boundary:** non-cyber software domains

Evidence-First Microtesting (EFM) is being investigated as a way to resolve consequential software-development assumptions with the smallest credible falsifiable experiments, independently inspect durable evidence, and adversarially test the measuring instrument before implementation expands.

This repository preserves the research history. It is intentionally not a claim that EFM is already a proven methodology.

## Research tracks

1. **EFM-native development** — begin with goal, decisions, assumptions, and evidence before meaningful architecture is committed.
2. **Prebugging** — use the method to search for latent defects and false confidence in existing software.
3. **Comparative studies** — compare EFM with ordinary development under frozen requirements and common evaluation.
4. **Negative/null cases** — retain cases where EFM adds cost without changing the result.
5. **Future-AI handoff durability** — test whether a fresh AI session can reconstruct and safely extend evidence-earned architecture without access to the original conversation.

## Protocol history

- `v0.1` governed experiments 001–003.
- `v0.2` added claim-scope hardening and post-green integration challenges.
- `v0.3` began with experiment 013 and added a prebuild completeness gate plus independent checking of nontrivial evaluator expectations.
- `PROTOCOL_REVIEW_AFTER_012.md` records the evidence that motivated v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` reviews three clean v0.3 runs and retains the protocol unchanged.

Earlier experiments keep their original classifications. Protocol changes are prospective rather than retroactive.

`FUTURE_AI_HANDOFF_STANDARD.md` is intentionally separate from the protocol: v0.3 governs how evidence is earned; the handoff standard governs how earned evidence is packaged for later AI sessions.

## Current evidence pattern

The repository now contains a mixed pattern rather than a simple success story:

- multiple EFM-native runs changed architecture before implementation;
- some EFM-native runs exposed implementation defects, overgeneralized microtests, or evaluator defects;
- clean v0.3 runs 013–015 all dispositioned consequential assumptions before code and independently checked important expectations;
- first evidence-earned implementations in 013–015 then survived integration/post-green testing without application rework;
- two controlled comparisons, 001 and 016, produced **null delivered-correctness results**: EFM generated more preimplementation evidence but the ordinary build-first arm independently delivered an equally correct first implementation;
- protocol-deviant runs are retained but excluded from clean-replication credit;
- evaluator failures are preserved separately rather than being misreported as candidate failures;
- Fresh-Context Reconstruction Test 001 produced a **96/100 strong pass** on another AI platform: the fresh model reconstructed DAGPlan's goal, A1–A6 evidence chains, E2/E3/E5 boundaries, and the crucial distinction between evidence-conflicting changes and an unproven DFS alternative.

No E0–E6 level is converted into a confidence percentage, and no universal EFM score is used.

## Current interpretation

The evidence increasingly supports a **scope claim**, not a universal development claim. EFM appears most defensible when a consequential assumption is genuinely uncertain and can alter architecture, reliability, or expensive downstream work. The controlled null results show that producing more evidence is not itself enough: on bounded tasks, a careful ordinary implementation may reach the same correct design with less process.

For the user's intended application, another important practical claim is emerging: an EFM record can preserve enough reasoning for a fresh AI session to understand why a strange or guide-less application was architected a certain way. Test 001 supports that claim preliminarily, but also showed that a reduced prose-only handoff is weaker than a package containing the runnable microtests, integration suite, oracle, judge, and post-green challenge.

The dominant scientific limitation remains research independence. These studies are still largely same-investigator/model and investigator-designed. The repository has no independent E4 methodology reproduction and no representative operational E6 evidence.

## Repository map

- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — current method; v0.3 retained unchanged after experiment 015.
- `PROTOCOL_REVIEW_AFTER_012.md` — evidence-based review leading to v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` — review retaining v0.3 unchanged and redirecting the next phase toward stronger research design.
- `FUTURE_AI_HANDOFF_STANDARD.md` — artifact-packaging standard for future AI continuity.
- `METRICS.md` — descriptive measurements collected across studies.
- `experiments/` — append-only experiment history.
- `templates/FUTURE_AI_HANDOFF.md` — reusable future-AI handoff map.
- `reconstruction/TEST_001_DAGPLAN_RESULT.md` — first scored cross-platform fresh-context reconstruction result.
- `results/INTERIM_SYNTHESIS_AFTER_016.md` — current evidence synthesis and limitations.
- `replication/BLIND_START_PACKET.md` — standalone protocol packet for a new investigator/model without exposing prior outcomes.
- `replication/INDEPENDENT_REPRODUCTION_BRIEF.md` — independence, instrumentation, artifact, and E4-review requirements.
- `replication/REPLICATION_RESULT_TEMPLATE.md` — structured submission template for an independent run.

## Active continuation

New work remains restricted to non-cyber software domains. Historical material remains preserved but is not being expanded into cybersecurity research.

Experiment 016 completed the recommended preregistered controlled comparison and produced a null correctness/rework result: both frozen line-mapper implementations passed 20,590 common checks plus 161,669 fresh post-green checks with zero candidate failures. EFM rejected a plausible `splitlines()` architecture before code, but build-first independently selected the same correct explicit scanner.

The first future-AI durability test has now passed strongly. The next handoff test uses a fuller runnable DAGPlan package to test whether a fresh AI can not only reconstruct the reasoning but reproduce the evidence and formulate a safe continuation plan for consequential changes.

Until independent or representative operational evidence exists, no E4 methodology, E6 operational, universal superiority, or statistical-significance claim is warranted.
