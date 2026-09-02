# Pipeline Lab Microplane Current State

Plane-ID: `MP-PIPELINE-LAB-20260902`
Checkpoint: `CP-20260902-002`
Updated: `2026-09-02`

## Goal
Determine the smallest reliable content-pipeline architecture by testing consequential assumptions before creating a production `content-pipeline` build. The immediate problem is whether semantic extraction from a real source transcript can be done cheaply and well enough to satisfy the existing independent judge.

## Governing authority and boundaries
- `EFMResearch` develops the method.
- `pipeline-lab` applies the method to the content-pipeline problem.
- A future production `content-pipeline` remains separate and is not authorized until the lab reaches `GO`.
- The source discussed at this checkpoint is owner-confirmed as coming from a public YouTube channel.
- Remote repository state outranks the earlier conversational reconstruction where the two differ; local working-copy cleanliness is still unknown unless directly checked.

## What exists now
- Private repository `specimenHQ/pipeline-lab` is directly accessible again through the connected GitHub app — `EV-20260902-011`.
- Remote `main` currently points at `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c` (`Record local semantic CPU path failure`) — `EV-20260902-011`.
- The remote history and EXP-003 README corroborate the reported sequence: minimal orchestration selected; analytical judge/reference calibrated; deterministic extraction killed; local Qwen3 4B CPU execution path killed; hosted semantic testing is the next admitted route — `EV-20260902-011`.
- The exact human-calibrated reference, semantic prompt, and scorer are recoverable from the repository. The reference contains four `PROMOTE` targets, one `HOLD`, one entertainment `REJECT`, source word count 4,635, and frozen SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435` — `EV-20260902-011`.
- The exact full transcript/public YouTube locator is not yet preserved in the Microplane package, while the scorer requires that transcript as an input — `EV-20260902-012`.

## Evidence-earned constraints
- Do not retry the same local Qwen CPU path without materially changed execution conditions — `D-20260902-005`.
- Do not replace the selected minimal orchestrator with Hermes or another agent framework merely to obtain one semantic extraction result — `D-20260902-006`.
- Do not run or score a hosted candidate against a reconstructed transcript unless it matches the frozen source digest — `EV-20260902-012`.
- Do not infer local worktree cleanliness from remote GitHub state.

## Active uncertainty
- `Q-20260902-005`: Can one bounded, inexpensive cloud semantic extractor satisfy the existing EXP-003 judge on the real transcript?
- `Q-20260902-007`: Can the exact public-source transcript be reacquired and verified against the frozen digest?

`Q-20260902-006` is answered for remote continuation: the authoritative remote repo and current `main` baseline are verified.

## Next bounded action
Reacquire the exact public YouTube source/transcript and verify that the preserved transcript text matches SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435`. Only then run one tightly capped hosted semantic candidate using the recovered frozen prompt and score it with the recovered independent scorer. Do not redesign the pipeline first.
