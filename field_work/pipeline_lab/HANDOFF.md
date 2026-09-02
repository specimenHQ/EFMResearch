# Pipeline Lab Microplane Handoff

Plane-ID: `MP-PIPELINE-LAB-20260902`
Checkpoint: `CP-20260902-001`
Updated: `2026-09-02`

This is a reconstruction map, not the authoritative evidence store.

## Goal
Use EFM to determine the smallest reliable content-pipeline architecture before production implementation, with the immediate focus on whether a cheap semantic cloud extractor can pass the existing EXP-003 judge on a real transcript.

## Where things stand
The last reported lab state is preserved as `EV-20260902-008`, but it came from the owner's supplied prior work transcript and is intentionally not promoted to independently verified Git state. The reported milestone includes Minimal Python + SQLite selected as orchestrator, deterministic extraction killed at 1/4 recall, the local Qwen3 4B CPU path killed, and reported pushed commit `8f2adfe`.

The current connected GitHub context cannot locate `pipeline-lab` — `EV-20260902-009`. That is an access/provenance boundary, not evidence that the repo is gone.

## Decisions currently in force
- `D-20260902-004` — keep EFMResearch, pipeline-lab, and future production content-pipeline roles separate.
- `D-20260902-005` — do not retry the same killed local Qwen CPU path without materially changed conditions.
- `D-20260902-006` — next model work remains one bounded cloud semantic-extraction test; Hermes is not promoted to orchestrator by convenience.

## Open questions
- `Q-20260902-005` — can a cheap cloud extractor pass the existing judge?
- `Q-20260902-006` — what is the authoritative current pipeline-lab repo/working-copy baseline?

## Next bounded action
Reacquire the authoritative EXP-003 fixture/judge and verify the current repository checkpoint. Then run exactly one bounded cloud extraction candidate and score it with the existing judge. Preserve raw input/output, model/route, cost or token usage if available, elapsed time, and judge result before making an architecture decision.

## Do not assume
- Reported commit `8f2adfe` is still current until verified.
- A cloud model is good enough merely because the local path failed.
- Hermes should become the orchestrator merely because it can call a cloud model.
- The public YouTube origin changes the need to preserve exact experiment provenance.
- Microplane has succeeded merely because this package now exists.

## Read order
1. `CURRENT_STATE.md`
2. active entries in `OPEN_QUESTIONS.md`
3. `EV-20260902-008` through `EV-20260902-010`
4. `D-20260902-004` through `D-20260902-006`
5. `artifacts/BASELINE_RECONSTRUCTION_2026-09-02.md`
