# Evidence-First Microtesting (EFM)

**Status:** exploratory research repository  
**Current protocol:** `0.1 — Frozen for initial replication`  
**Date frozen:** 2026-08-31

Evidence-First Microtesting (EFM) is being investigated as a way to resolve dangerous software-development assumptions with the smallest credible falsifiable experiments, independently inspect durable evidence, and adversarially test the measuring instrument before implementation expands.

This repository exists to preserve the research history. It is intentionally not a claim that EFM is already a proven methodology.

## Research tracks

1. **EFM-native development** — begin with goal, decisions, assumptions, and evidence before meaningful architecture is committed.
2. **Prebugging** — apply EFM adversarially to software developed by ordinary methods to search for latent defects and false confidence.
3. **Comparative studies** — compare EFM with ordinary development under frozen requirements and common evaluation.
4. **Negative/null cases** — record cases where EFM adds cost without changing the result.

## Repository map

- `RESEARCH_AGENDA.md` — original v0.1 exploratory agenda, preserved as the historical starting point.
- `PROTOCOL.md` — frozen procedure for the next replication phase.
- `METRICS.md` — measurements to collect consistently.
- `experiments/001-neutral-timestamp/` — first neutral comparison; EFM added confidence but did not improve the delivered result.
- `experiments/002-slotlock/` — first EFM-native build; EFM influenced architecture and exposed a false conflict classification during integration.
- `templates/` — records to use for future experiments.
- `prebugging/` — future adversarial studies on existing software.
- `results/` — aggregate results only after enough comparable studies exist.

## Research rule

Negative results stay in the repository. Protocol changes are versioned and dated rather than silently rewriting prior experiments.

## Current next experiment

Run EFM-native build #003 in a domain materially different from SlotLock, using `PROTOCOL.md` without changing it during the experiment.
