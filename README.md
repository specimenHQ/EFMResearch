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

## Protocol history

- `v0.1` governed experiments 001–003.
- `v0.2` added claim-scope hardening and post-green integration challenges.
- `v0.3` began with experiment 013 and added a prebuild completeness gate plus independent checking of nontrivial evaluator expectations.
- `PROTOCOL_REVIEW_AFTER_012.md` records the evidence that motivated v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` reviews three clean v0.3 runs and retains the protocol unchanged.

Earlier experiments keep their original classifications. Protocol changes are prospective rather than retroactive.

## Current evidence pattern

The repository now contains a mixed pattern rather than a simple success story:

- multiple EFM-native runs changed architecture before implementation;
- some EFM-native runs exposed implementation defects, overgeneralized microtests, or evaluator defects;
- clean v0.3 runs 013–015 all dispositioned consequential assumptions before code and independently checked important expectations;
- first evidence-earned implementations in 013–015 then survived integration/post-green testing without application rework;
- two controlled comparisons, 001 and 016, produced **null delivered-correctness results**: EFM generated more preimplementation evidence but the ordinary build-first arm independently delivered an equally correct first implementation;
- protocol-deviant runs are retained but excluded from clean-replication credit;
- evaluator failures are preserved separately rather than being misreported as candidate failures.

No E0–E6 level is converted into a confidence percentage, and no universal EFM score is used.

## Current interpretation

The evidence increasingly supports a **scope claim**, not a universal development claim. EFM appears most defensible when a consequential assumption is genuinely uncertain and can alter architecture, reliability, or expensive downstream work. The controlled null results show that producing more evidence is not itself enough: on bounded tasks, a careful ordinary implementation may reach the same correct design with less process.

The dominant limitation is now research independence. These studies are still largely same-investigator/model and investigator-designed. The repository has no independent E4 methodology reproduction and no representative operational E6 evidence.

## Repository map

- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — current method; v0.3 retained unchanged after experiment 015.
- `PROTOCOL_REVIEW_AFTER_012.md` — evidence-based review leading to v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` — review retaining v0.3 unchanged and redirecting the next phase toward stronger research design.
- `METRICS.md` — descriptive measurements collected across studies.
- `experiments/` — append-only experiment history.
- `templates/` — reusable experiment records.
- `prebugging/` — separate methodological track.
- `results/` — aggregate/interim synthesis after enough comparable evidence exists.

## Active continuation

New work remains restricted to non-cyber software domains. Historical material remains preserved but is not being expanded into cybersecurity research.

Experiment 016 completed the recommended preregistered controlled comparison and produced a null correctness/rework result: both frozen line-mapper implementations passed 20,590 common checks plus 161,669 fresh post-green checks with zero candidate failures. EFM rejected a plausible `splitlines()` architecture before code, but build-first independently selected the same correct explicit scanner.

The highest-information next step is **independent reproduction or representative real-project use**, not another same-investigator bounded toy build. Until that evidence exists, no E4 methodology, E6 operational, superiority, or statistical-significance claim is warranted.
