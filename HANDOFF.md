# EFM Handoff

Updated: `2026-09-02`

This is a reconstruction map, not the authoritative evidence store.

## Goal
Use EFM as an evidence-first way to build under uncertainty while preserving enough durable provenance that future humans or AI agents can understand what was learned, why decisions changed, and what remains unknown.

## Where things stand
EFM has accumulated controlled experiments and fresh-context handoff evidence. The current direction is continuity-first field use: apply EFM during real projects, record bounded observations as they occur, and let the longitudinal record—not an ever-expanding laboratory program alone—show where the method helps, fails, or adds unnecessary cost.

The first continuity format is defined in `CONTINUITY_STANDARD.md`.

## Evidence that currently governs the work
- `EV-20260902-001` — live use makes continuity/stable carry-over an immediate operational requirement.
- `EV-20260902-002` — prior handoff tests support durable artifact transfer across fresh AI contexts in the tested cases.

## Decisions currently in force
- `D-20260902-001` — use longitudinal real-world work as a primary learning path; controlled microtests remain available when useful.
- `D-20260902-002` — trial the five-file continuity layer.

## Open questions
- `Q-20260902-001` — whether the five-file format remains useful and maintainable in actual ongoing projects.

## Next action
Apply the continuity templates prospectively to current field work. Record new observations at the time they affect a decision rather than reconstructing them later from conversation history.

## Do not assume
- EFM has been scientifically validated as universally superior.
- Field observations automatically establish causality.
- Controlled microtesting has been abandoned; it remains a tool when isolation matters.
- The five-file format is final. It is currently provisional and should earn its permanence through use.

## Read order
1. `CURRENT_STATE.md`
2. `OPEN_QUESTIONS.md`
3. relevant entries in `EVIDENCE_LEDGER.md`
4. relevant entries in `DECISIONS.md`
5. `CONTINUITY_STANDARD.md`
6. raw/research artifacts referenced by those records
