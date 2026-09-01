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

The repository contains both positive and negative methodological evidence:

- small bounded work can pass equally well without EFM, producing a useful null result;
- multiple EFM-native runs changed architecture before implementation;
- some first green implementations survived post-green challenges without rework;
- some runs exposed false confidence in the implementation or in an earlier microtest;
- multiple runs exposed evaluator defects rather than application defects;
- protocol-deviant runs are retained but excluded from clean-replication credit;
- experiments 013–015 all passed the v0.3 prebuild completeness gate before code;
- alternate expectation checks were usable across scheduling, dependency planning, and text transformation;
- experiment 015 caught and rejected a defective adversarial judge before E3 evidence was accepted.

No E0–E6 level is converted into a confidence percentage, and no universal EFM score is used.

## Current limitation

The dominant limitation is now research design rather than another missing protocol rule. The studies are still largely same-investigator/model, investigator-designed synthetic tasks, with no independent E4 methodology reproduction and no operational E6 evidence. More EFM-native small builds alone now have diminishing information value.

## Repository map

- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — current method; v0.3 retained unchanged after experiment 015.
- `PROTOCOL_REVIEW_AFTER_012.md` — evidence-based review leading to v0.3.
- `PROTOCOL_REVIEW_AFTER_015.md` — frozen-block review retaining v0.3 unchanged and redirecting the next phase toward controlled comparison.
- `METRICS.md` — descriptive measurements collected across studies.
- `experiments/` — append-only experiment history.
- `templates/` — reusable experiment records.
- `prebugging/` — separate methodological track.
- `results/` — aggregate results only after enough comparable studies exist.

## Active continuation

New work remains restricted to non-cyber software domains. Historical material remains preserved but is not being expanded into cybersecurity research.

Experiments 013 WallClock, 014 DAGPlan, and 015 SpanEdit completed the first frozen v0.3 block as clean EFM-native E5 studies. Protocol review found no reason to create v0.4. The preferred next experiment is **016: a preregistered medium-consequence controlled comparison**, with the build-first implementation frozen before any EFM microtests, both arms frozen before a common adversarial evaluation, and null results preserved if the ordinary arm performs equally well.
