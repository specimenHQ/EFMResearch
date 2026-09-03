# Pipeline Lab Microplane Current State

Plane-ID: `MP-PIPELINE-LAB-20260902`
Checkpoint: `CP-20260902-003`
Updated: `2026-09-02`

## Goal
Determine the smallest reliable content-pipeline architecture by testing consequential assumptions before creating a production `content-pipeline` build. The immediate problem is whether semantic extraction from a real source transcript can be done cheaply and well enough to satisfy the existing independent judge.

## Governing authority and boundaries
- `EFMResearch` develops the method.
- `pipeline-lab` applies the method to the content-pipeline problem.
- A future production `content-pipeline` remains separate and is not authorized until the lab reaches `GO`.
- The exact public source locator is now preserved as YouTube video `UcBH6MCAst8`: `https://youtu.be/UcBH6MCAst8?si=0AZSUVQwKja3yhdu` — `EV-20260902-013`.
- Remote repository state outranks the earlier conversational reconstruction where the two differ; local working-copy cleanliness is still unknown unless directly checked.

## What exists now
- Private repository `specimenHQ/pipeline-lab` is directly accessible through the connected GitHub app — `EV-20260902-011`.
- Remote `main` points at `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c` (`Record local semantic CPU path failure`) at the verified checkpoint — `EV-20260902-011`.
- The remote history and EXP-003 README corroborate the sequence: minimal orchestration selected; analytical judge/reference calibrated; deterministic extraction killed; local Qwen3 4B CPU execution path killed; hosted semantic testing is the next admitted route — `EV-20260902-011`.
- The exact human-calibrated reference, semantic prompt, and scorer are recoverable from the repository. The reference contains four `PROMOTE` targets, one `HOLD`, one entertainment `REJECT`, source word count 4,635, and frozen SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435` — `EV-20260902-011`.
- The exact public video is now identified as Red Letter Media's `What Are Next for Star Trek?`, video ID `UcBH6MCAst8` — `EV-20260902-013`.
- Full transcript text has not yet been reacquired and hash-verified. The source-identity problem is resolved; the source-text verification problem remains — `EV-20260902-013`.

## Evidence-earned constraints
- Do not retry the same local Qwen CPU path without materially changed execution conditions — `D-20260902-005`.
- Do not replace the selected minimal orchestrator with Hermes or another agent framework merely to obtain one semantic extraction result — `D-20260902-006`.
- Do not run or score a hosted candidate against a reconstructed transcript unless it matches the frozen source digest — `EV-20260902-012`, `EV-20260902-013`.
- Do not infer local worktree cleanliness from remote GitHub state.

## Active uncertainty
- `Q-20260902-005`: Can one bounded, inexpensive cloud semantic extractor satisfy the existing EXP-003 judge on the real transcript?
- `Q-20260902-007`: Can transcript text from exact video `UcBH6MCAst8` be reacquired and verified against the frozen digest? The locator portion is resolved; text/digest verification remains open.

`Q-20260902-006` is answered for remote continuation: the authoritative remote repo and current `main` baseline are verified.

## Next bounded action
Retrieve transcript/caption text from exact YouTube video `UcBH6MCAst8`, preserve the raw text form, and compute SHA-256 using the same UTF-8 text rule as the existing verifier. If it matches `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435`, run exactly one tightly capped hosted semantic candidate using the frozen prompt and score it with the recovered independent scorer. Do not redesign the pipeline first.
