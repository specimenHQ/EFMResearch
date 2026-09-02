# Pipeline Lab Microplane Current State

Plane-ID: `MP-PIPELINE-LAB-20260902`
Checkpoint: `CP-20260902-001`
Updated: `2026-09-02`

## Goal
Determine the smallest reliable content-pipeline architecture by testing consequential assumptions before creating a production `content-pipeline` build. The immediate problem is whether semantic extraction from a real source transcript can be done cheaply and well enough to satisfy the existing independent judge.

## Governing authority and boundaries
- `EFMResearch` develops the method.
- `pipeline-lab` applies the method to the content-pipeline problem.
- A future production `content-pipeline` remains separate and is not authorized until the lab reaches `GO`.
- The source discussed at this checkpoint is owner-confirmed as coming from a public YouTube channel.
- Historical state reconstructed from conversation is orientation evidence, not independent verification of the current repository.

## What exists now
- Last reported lab milestone: Minimal Python + SQLite selected as orchestrator; content-quality judge calibrated; real analytical reference created; deterministic extraction baseline killed at 1/4 recall; local Qwen3 4B CPU path killed; documentation corrections committed and pushed as reported commit `8f2adfe` — `EV-20260902-008`.
- The connected GitHub app currently does not expose a `pipeline-lab` repository, so that reported commit/worktree state cannot be independently checked here — `EV-20260902-009`.
- This second live Microplane package was created because EFM's active continuity question explicitly calls for another ongoing project beyond Resiimark — `EV-20260902-010`.

## Evidence-earned constraints
- Do not retry the same local Qwen CPU path without materially changed execution conditions — `D-20260902-005`.
- Do not replace the selected minimal orchestrator with Hermes or another agent framework merely to obtain one semantic extraction result — `D-20260902-006`.
- Do not claim the last reported Git state is current until the authoritative repo or working copy is reacquired.

## Active uncertainty
`Q-20260902-005`: Can one bounded, inexpensive cloud semantic extractor satisfy the existing EXP-003 judge on the real transcript?

## Next bounded action
Reacquire the authoritative EXP-003 fixture, judge, and current `pipeline-lab` state. Once those exact artifacts are verified, run one cloud semantic extraction candidate with a declared cost/token boundary and score its preserved output using the existing independent judge. Do not redesign the pipeline first.
