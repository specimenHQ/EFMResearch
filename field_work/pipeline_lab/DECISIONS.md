# Pipeline Lab Microplane Decisions

Plane-ID: `MP-PIPELINE-LAB-20260902`
Append only. Supersede by adding a later decision; do not rewrite history.

## D-20260902-004
- Date: `2026-09-02`
- Status: `active — reconstructed from explicit prior owner direction`
- Decision: Keep the repositories conceptually separate: `EFMResearch` is the methodology repository, `pipeline-lab` is the applied research project, and a production `content-pipeline` is created only after a lab `GO` decision.
- Evidence/basis: `EV-20260902-008`; owner-supplied prior transcript.
- Alternatives: merge methodology and application histories; start production implementation now.
- Reversal condition: explicit owner change of project structure or new evidence that separation materially prevents the research goal.
- Supersedes: none.

## D-20260902-005
- Date: `2026-09-02`
- Status: `active — evidence-based, pending artifact recheck`
- Decision: Keep the previously tested local Qwen3 4B CPU execution path classified `KILL`. Do not retry the same path simply because cloud access is inconvenient.
- Evidence/basis: `EV-20260902-008`.
- Alternatives: rerun the same local model path; install a larger local Hermes model.
- Reversal condition: materially different hardware, acceleration, context strategy, or other execution condition that directly addresses the observed boundary.
- Supersedes: none.

## D-20260902-006
- Date: `2026-09-02`
- Status: `provisional — next-test routing decision`
- Decision: The next model experiment should remain a bounded cloud semantic-extraction test against the existing EXP-003 judge. Hermes, if used, is a candidate extractor route only; it does not replace the selected Minimal Python + SQLite orchestrator without new evidence.
- Evidence/basis: `EV-20260902-008` and the existing separation between extractor evaluation and orchestration.
- Alternatives: redesign around Hermes; add a new agent framework; continue deterministic extraction work already reported as inadequate.
- Reversal condition: the authoritative EXP-003 artifacts show this test was already completed, or new evidence shows the judge/fixture no longer tests the consequential uncertainty.
- Supersedes: none.
