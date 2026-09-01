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
- `v0.3` begins with experiment 013 and adds a prebuild completeness gate plus independent checking of nontrivial evaluator expectations.
- `PROTOCOL_REVIEW_AFTER_012.md` records the evidence that motivated v0.3.

Earlier experiments keep their original classifications. Protocol changes are prospective rather than retroactive.

## Current evidence pattern

The repository now contains both positive and negative methodological evidence:

- small bounded work can pass equally well without EFM, producing a useful null result;
- multiple EFM-native runs changed architecture before implementation;
- some first green implementations survived post-green challenges without rework;
- some runs exposed false confidence in the implementation or in an earlier microtest;
- multiple runs exposed evaluator defects rather than application defects;
- protocol-deviant runs are retained but excluded from clean-replication credit;
- experiment 013 demonstrated the new v0.3 gates cleanly in a scheduling/timezone domain;
- experiment 014 repeated the v0.3 pattern in dependency planning: all admitted consequential assumptions were tested before code, a nontrivial expectation was independently derived, and the first implementation survived integration plus a 720-permutation post-green challenge without rework.

No E0–E6 level is converted into a confidence percentage, and no universal EFM score is used.

## Repository map

- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — current prospective procedure.
- `PROTOCOL_REVIEW_AFTER_012.md` — evidence-based protocol review leading to v0.3.
- `METRICS.md` — descriptive measurements collected across studies.
- `experiments/` — append-only experiment history.
- `templates/` — reusable experiment records.
- `prebugging/` — separate methodological track.
- `results/` — aggregate results only after enough comparable studies exist.

## Active continuation

New work is restricted to non-cyber software domains such as data transformation, numerical logic, scheduling, state machines, local application behavior, and ordinary file/data processing. Historical material remains preserved but is not being expanded into cybersecurity research.

Experiments 013 WallClock and 014 DAGPlan are complete as clean Protocol-v0.3 EFM-native runs, each accepted at E5 within its tested scope. The next prospective replication is experiment 015 under the unchanged frozen v0.3 protocol; protocol review follows after 015.
