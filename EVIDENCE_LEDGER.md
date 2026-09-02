# EFM Evidence Ledger

Append only. Corrections and later interpretations must be added as new records rather than rewriting prior evidence.

## EV-20260902-001
- Date: `2026-09-02`
- Question/assumption: What is the immediate operational problem for EFM as it moves from controlled study into ongoing real projects?
- Observation: EFM is currently being used during live Shopify work, where decisions and observations arrive incrementally rather than as a single frozen experiment. The immediate failure risk is loss of context, provenance, and decision history across sessions/tools rather than inability to design another laboratory test.
- Source/artifact: Field-use observation recorded contemporaneously in this ledger; Shopify artifacts live outside this repository.
- Strength: `E1 — Observation`
- Supports: Continuity and stable evidence carry-over are practical requirements for ongoing EFM field use.
- Does not establish: That EFM is effective in Shopify, that EFM outperforms ordinary development, or that laboratory testing is unnecessary in every case.
- Project consequence: Prioritize a minimal continuity/storage layer and evaluate it through real use.
- Supersedes/corrects: `none`

## EV-20260902-002
- Date: `2026-09-02`
- Question/assumption: Can durable EFM artifacts transfer useful state to a fresh AI without the original conversation?
- Observation: Prior fresh-context handoff tests recovered project goal, evidence boundaries, architecture reasoning, change-impact logic, and evaluator provenance at high fidelity; those tests also showed that runnable/raw evidence should remain available behind summaries.
- Source/artifact: `FUTURE_AI_HANDOFF_STANDARD.md` and `handoff_tests/`
- Strength: `E3` for the tested handoff/evaluator cases; not E4 methodology reproduction or E6 operational evidence.
- Supports: Durable structured artifacts can preserve useful EFM reasoning across fresh AI contexts in the tested cases.
- Does not establish: That the new five-file continuity format is sufficient for long-running real-world projects.
- Project consequence: Build the lighter continuity layer on top of the existing handoff lesson: summaries point to durable evidence rather than replacing it.
- Supersedes/corrects: `none`

## EV-20260902-006
- Date: `2026-09-02`
- Question/assumption: Can the five-file continuity layer be instantiated prospectively during live Shopify work while preserving evidence boundaries instead of reconstructing conclusions from conversation memory?
- Observation: During live Resiimark Shopify work, a dedicated package was created under `field_work/resiimark/` containing `CURRENT_STATE.md`, `EVIDENCE_LEDGER.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `HANDOFF.md`, and a raw Shopify baseline artifact. When Shopify tools exposed two different domain strings, the analytics were temporarily withheld from the evidence ledger until an authenticated Shopify GraphQL identity check established that both domains belonged to the same shop. Prior supplier cost observations that were not independently recaptured were explicitly left unknown rather than reconstructed from memory.
- Source/artifact: `field_work/resiimark/HANDOFF.md`, `field_work/resiimark/EVIDENCE_LEDGER.md`, `field_work/resiimark/artifacts/SHOPIFY_BASELINE_2026-09-02.md`
- Strength: `E1 — Observation` of initial live continuity use.
- Supports: The five-file format can be applied prospectively during live work and can preserve provenance, claim boundaries, and unresolved evidence at this initial checkpoint.
- Does not establish: That the format remains maintainable over time, that a fresh AI can yet reconstruct Resiimark correctly from the package alone, or that EFM improves Shopify outcomes relative to ordinary work.
- Project consequence: `Q-20260902-001` now has its first live prospective instance. Continue maintaining the Resiimark package through at least one consequential product decision, then test fresh-context reconstruction rather than treating initial creation as validation.
- Supersedes/corrects: `none`

## EV-20260902-007
- Date: `2026-09-02`
- Question/assumption: Can the continuity layer be applied to a second ongoing project while keeping reconstructed conversational history visibly separate from independently verified project state?
- Observation: A second field package was created at `field_work/pipeline_lab/`. The owner's supplied prior pipeline-lab transcript was preserved as a bounded baseline reconstruction, while a current GitHub connector check that could not resolve `pipeline-lab` was recorded as a separate observation rather than being used to erase or confirm the historical report. The package leaves the current repository baseline explicitly unresolved and names reacquisition of the authoritative EXP-003 artifacts as the next action.
- Source/artifact: `field_work/pipeline_lab/HANDOFF.md`, `field_work/pipeline_lab/EVIDENCE_LEDGER.md`, `field_work/pipeline_lab/artifacts/BASELINE_RECONSTRUCTION_2026-09-02.md`
- Strength: `E1 — Observation` of a second live continuity instantiation.
- Supports: The five-file/Microplane format can represent a second domain and can preserve a provenance conflict between reported history and present tool visibility without silently resolving it.
- Does not establish: Long-term maintainability, fresh-context adequacy, or superiority over simpler notes.
- Project consequence: `Q-20260902-001` now has two live field instances. The next useful evidence is prospective maintenance through consequential decisions and later fresh-context reconstruction, not more template creation.
- Supersedes/corrects: `none`
