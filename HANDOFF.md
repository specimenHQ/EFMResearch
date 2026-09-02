# EFM Handoff

Updated: `2026-09-02`

This is a reconstruction map, not the authoritative evidence store.

## Goal
Use EFM as an evidence-first way to build under uncertainty while preserving enough durable provenance that future humans or AI agents can understand what was learned, why decisions changed, and what remains unknown.

## Where things stand
EFM has accumulated controlled experiments and fresh-context handoff evidence. The current direction is continuity-first field use: apply EFM during real projects, record bounded observations as they occur, and let the longitudinal record—not an ever-expanding laboratory program alone—show where the method helps, fails, or adds unnecessary cost.

The first continuity format is defined in `CONTINUITY_STANDARD.md`.

Two live field packages now exercise it:
- `field_work/resiimark/` — prospective Shopify/prebugging case, `EV-20260902-006`.
- `field_work/pipeline_lab/` — content-pipeline case, `EV-20260902-007`, with reconstructed prior conversation state kept explicitly separate from current repository verification.

## Evidence that currently governs the work
- `EV-20260902-001` — live use makes continuity/stable carry-over an immediate operational requirement.
- `EV-20260902-002` — prior handoff tests support durable artifact transfer across fresh AI contexts in the tested cases.
- `EV-20260902-006` — first live continuity package can preserve provenance and unresolved evidence at initial checkpoint.
- `EV-20260902-007` — a second live package can preserve a provenance conflict without silently resolving it.

## Decisions currently in force
- `D-20260902-001` — use longitudinal real-world work as a primary learning path; controlled microtests remain available when useful.
- `D-20260902-002` — trial the five-file continuity layer.

## Open questions
- `Q-20260902-001` — whether the five-file format remains useful and maintainable in actual ongoing projects.

## Next action
Maintain the two live packages through consequential decisions. In pipeline-lab, reacquire the authoritative EXP-003 artifacts and perform the next bounded cloud semantic-extraction test rather than redesigning architecture from conversational memory. In Resiimark, continue through a consequential supplier/product decision. Then test fresh-context reconstruction from durable packages alone.

## Do not assume
- EFM has been scientifically validated as universally superior.
- Field observations automatically establish causality.
- Controlled microtesting has been abandoned; it remains a tool when isolation matters.
- The five-file format is final. It is currently provisional and should earn its permanence through use.
- A historical conversation reconstruction is equivalent to a verified current repository state.

## Read order
1. `CURRENT_STATE.md`
2. `OPEN_QUESTIONS.md`
3. relevant entries in `EVIDENCE_LEDGER.md`
4. relevant entries in `DECISIONS.md`
5. `CONTINUITY_STANDARD.md`
6. the relevant field package under `field_work/`
