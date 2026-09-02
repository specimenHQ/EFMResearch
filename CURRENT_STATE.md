# EFM Current State — 2026-09-02

## Goal
Use evidence-first reasoning during real work so consequential assumptions are challenged before they harden into expensive decisions, while preserving enough durable context that future humans or AI agents can continue from evidence rather than conversation memory.

## Exists now
- Protocol v0.3 remains preserved.
- `FUTURE_AI_HANDOFF_STANDARD.md` preserves the fuller reproducibility/handoff standard.
- `CONTINUITY_STANDARD.md` v0.1 now defines a lighter operational storage layer for ongoing field use.
- The EFMResearch repo itself now uses five continuity files: `CURRENT_STATE.md`, `EVIDENCE_LEDGER.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, and `HANDOFF.md`.
- Reusable project templates live under `templates/continuity/`.

## Evidence-earned beliefs
- Durable artifacts have transferred important EFM reasoning across fresh AI contexts in prior handoff tests — `EV-20260902-002`.
- Current live use makes stable carry-over of observations and decisions an immediate operational requirement — `EV-20260902-001`.

## Active direction
EFM is moving from a lab-centered validation mindset toward longitudinal field use. Controlled microtests remain available when a consequential uncertainty benefits from isolation, but they are one tool inside a broader loop:

`uncertainty -> smallest credible action -> observable result -> evidence -> decision -> updated state`

Current real-world use includes Shopify work, where the useful test is whether real store/product decisions survive contact with actual conditions rather than whether they pass a synthetic laboratory scenario.

## Next action
Use the five-file continuity format prospectively in live work and observe whether it preserves state without becoming burdensome. This is tracked as `Q-20260902-001`.

## Immediate cautions
- Do not claim EFM is universally validated or superior.
- Do not treat uncontrolled field observations as stronger evidence than they are.
- Do not silently rewrite negative/null history.
- The five-file format is provisional until field use shows it is durable and maintainable.
