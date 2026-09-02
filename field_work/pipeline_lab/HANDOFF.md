# Pipeline Lab Microplane Handoff

Plane-ID: `MP-PIPELINE-LAB-20260902`
Checkpoint: `CP-20260902-002`
Updated: `2026-09-02`

This is a reconstruction map, not the authoritative evidence store.

## Goal
Use EFM to determine the smallest reliable content-pipeline architecture before production implementation, with the immediate focus on whether a cheap hosted semantic extractor can pass the existing EXP-003 judge on the real public-source transcript.

## Where things stand
GitHub access is restored. The authoritative remote is private repository `specimenHQ/pipeline-lab`, branch `main`, with current remote commit `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c` (`Record local semantic CPU path failure`) — `EV-20260902-011`.

Direct repository reads recovered the current EXP-003 status plus the human-calibrated reference, frozen semantic prompt, and independent scorer. The local Qwen3 4B CPU execution path remains killed; model quality was never scored. The next admitted model path is one tightly capped hosted semantic call or a future verified accelerator — `EV-20260902-011`.

The remaining blocker is source provenance. The reference preserves the 4,635-word source digest `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435` and calibration targets, but the exact public YouTube URL/full transcript is not currently preserved here. The scorer requires the source transcript as input — `EV-20260902-012`.

## Decisions currently in force
- `D-20260902-004` — keep EFMResearch, pipeline-lab, and future production content-pipeline roles separate.
- `D-20260902-005` — do not retry the same killed local Qwen CPU path without materially changed conditions.
- `D-20260902-006` — next model work remains one bounded hosted semantic-extraction test; Hermes is not promoted to orchestrator by convenience.

## Open questions
- `Q-20260902-005` — can a cheap hosted extractor pass the existing judge?
- `Q-20260902-007` — can the exact public-source transcript be reacquired and verified against the frozen digest?

`Q-20260902-006` is answered for remote continuation.

## Next bounded action
Recover the exact YouTube source/transcript and verify the transcript text against SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435`. If it matches, run exactly one bounded hosted extraction candidate using the frozen prompt, preserve raw output/model/cost-or-token/elapsed metadata, and score it with the existing `score.py` before making any architecture decision.

## Do not assume
- The local worktree is clean because remote `main` is known.
- A hosted model is good enough merely because the local path failed.
- Hermes should become the orchestrator merely because it can call a cloud model.
- A similar transcript is interchangeable with the frozen source.
- Microplane has succeeded merely because this package can now resume work.

## Read order
1. `CURRENT_STATE.md`
2. active entries in `OPEN_QUESTIONS.md`
3. `EV-20260902-011` and `EV-20260902-012`
4. `D-20260902-004` through `D-20260902-006`
5. remote `pipeline-lab/EXPERIMENTS/EXP-003/README.md`
6. remote `pipeline-lab/EXPERIMENTS/EXP-003/real-reference-001.json`
7. remote `pipeline-lab/EXPERIMENTS/EXP-003/semantic-qwen3-4b/PROMPT.md`
8. remote `pipeline-lab/EXPERIMENTS/EXP-003/semantic-qwen3-4b/score.py`
