# Pipeline Lab Microplane Evidence Ledger

Plane-ID: `MP-PIPELINE-LAB-20260902`
Append only. Capture observation before interpretation.

## EV-20260902-008
- Date: `2026-09-02`
- Question/assumption: What was the last reported pipeline-lab state before this Microplane checkpoint?
- Observation: The owner supplied a prior work transcript reporting that Minimal Python + SQLite had been selected as orchestrator, the content-quality judge had been calibrated, a real analytical reference had been created, the deterministic extraction baseline had been killed at 1/4 recall, and the local Qwen3 4B CPU path had been killed after an unusably slow/oversized run. The transcript reports that stale documentation was corrected and commit `8f2adfe` (`Record local semantic CPU path failure`) was pushed with a clean worktree.
- Source/artifact: `artifacts/BASELINE_RECONSTRUCTION_2026-09-02.md`; owner-supplied prior conversation transcript in the 2026-09-02 ChatGPT session.
- Source durability: preserved in this field package as a bounded reconstruction; underlying repository not yet reverified from this tool context.
- Freshness/recheck: recheck required before editing or relying on exact current Git state.
- Strength: `E1 — reported historical observation / reconstruction`.
- Supports: orientation to the last reported decision state and avoidance of repeating already-failed paths.
- Does not establish: that `8f2adfe` is still HEAD, that the worktree is currently clean, or that every reported benchmark detail is reproducible from preserved raw artifacts.
- Project consequence: preserve the reported milestone as provisional baseline; verify exact experiment artifacts before the next model run.
- Conflict status: none known; current repository visibility is unresolved by `EV-20260902-009`.

## EV-20260902-009
- Date: `2026-09-02`
- Question/assumption: Can the current connected GitHub context independently verify the authoritative `pipeline-lab` repository now?
- Observation: A direct lookup for `specimenHQ/pipeline-lab` returned not found, repository searches returned no `pipeline-lab`, and the connected account's visible `specimenHQ` repository list did not include it.
- Source/artifact: connected GitHub tool observations from the 2026-09-02 Microplane continuation session.
- Source durability: current tool observation; preserve this entry as the result of this access attempt.
- Freshness/recheck: current as of 2026-09-02; recheck when repository URL, installation scope, or local working copy is available.
- Strength: `E1 — direct access observation`.
- Supports: this ChatGPT context could not verify or modify `pipeline-lab` through the connected GitHub app at that attempt.
- Does not establish: that the repository was deleted, never existed, is not private elsewhere, or that the local working copy is unavailable.
- Project consequence: do not claim exact current repo state until access is restored.
- Conflict status: superseded operationally by later access evidence `EV-20260902-011`; the failed access attempt remains historical evidence.

## EV-20260902-010
- Date: `2026-09-02`
- Question/assumption: Is pipeline-lab an appropriate second live continuity case for the current EFM field phase?
- Observation: EFMResearch `CURRENT_STATE.md` says the five-file format should be applied to another ongoing project before permanence is decided, and `Q-20260902-001` explicitly names that as a next observable.
- Source/artifact: repository-root `CURRENT_STATE.md`, `OPEN_QUESTIONS.md`, and `CONTINUITY_STANDARD.md` in `specimenHQ/EFMResearch`.
- Source durability: version-controlled repository artifacts.
- Freshness/recheck: current repository state as read on 2026-09-02.
- Strength: `E1 — project-state observation`.
- Supports: using the ongoing pipeline work as the second continuity field instance is aligned with the currently recorded EFM research direction.
- Does not establish: that Microplane is adequate, maintainable, or superior.
- Project consequence: instantiate and maintain this package prospectively from this checkpoint forward.
- Conflict status: none.

## EV-20260902-011
- Date: `2026-09-02`
- Question/assumption: After GitHub reconnection, can the authoritative remote pipeline-lab baseline and EXP-003 state be verified directly?
- Observation: The connected GitHub app now exposes private repository `specimenHQ/pipeline-lab`. The default branch is `main`; the newest remote commit returned is `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c`, message `Record local semantic CPU path failure`, dated 2026-09-01. Direct fetch of `EXPERIMENTS/EXP-003/README.md` confirms status `PHASE 3 — SEMANTIC NEED PROVEN; LOCAL CPU PATH KILLED` and says the next semantic test requires a verified GPU path or one tightly capped hosted semantic call. Direct fetches also recovered `real-reference-001.json`, the frozen semantic prompt, and `semantic-qwen3-4b/score.py`.
- Source/artifact: connected GitHub repository metadata and remote files in `specimenHQ/pipeline-lab`; commit `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c`; `EXPERIMENTS/EXP-003/README.md`; `EXPERIMENTS/EXP-003/real-reference-001.json`; `EXPERIMENTS/EXP-003/semantic-qwen3-4b/PROMPT.md`; `EXPERIMENTS/EXP-003/semantic-qwen3-4b/score.py`.
- Source durability: version-controlled GitHub remote.
- Freshness/recheck: verified from the connected remote on 2026-09-02.
- Strength: `E1 — direct repository observation`.
- Supports: the authoritative remote repository and remote `main` baseline are reacquired; the reported `8f2adfe` milestone is real and current on the remote; the exact reference, prompt, and scorer can now govern continuation.
- Does not establish: that any local working copy is clean or identical to remote `main`, or that a hosted semantic candidate will pass.
- Project consequence: close the repository-location uncertainty for remote continuation and proceed only from the recovered EXP-003 artifacts.
- Conflict status: resolves the access condition recorded in `EV-20260902-009` without deleting that failed observation.

## EV-20260902-012
- Date: `2026-09-02`
- Question/assumption: Is the exact real-source transcript/provenance currently sufficient to execute the scorer reproducibly?
- Observation: The recovered `real-reference-001.json` preserves source name, SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435`, word count `4635`, and the six calibration quotations, but it does not preserve a public YouTube URL or the full transcript text. The recovered scorer explicitly requires a transcript file as input. The owner's current statement establishes only that the source came from a public YouTube channel; the exact URL/source identity is not present in the current Microplane package or recovered prior context.
- Source/artifact: `EXPERIMENTS/EXP-003/real-reference-001.json`; `EXPERIMENTS/EXP-003/semantic-qwen3-4b/score.py`; owner statement in the 2026-09-02 continuation session; prior-context retrieval attempt.
- Source durability: repository artifacts are durable; exact public source locator remains unresolved.
- Freshness/recheck: current as of 2026-09-02; recheck immediately when the source URL or transcript is supplied.
- Strength: `E1 — direct artifact/provenance observation`.
- Supports: source reacquisition is the smallest remaining prerequisite before a reproducible hosted extraction run.
- Does not establish: that the transcript is absent from every local machine/archive or that the public source is unavailable.
- Project consequence: open `Q-20260902-007`; do not run or score a hosted candidate against a reconstructed transcript that has not been verified against the frozen digest.
- Conflict status: none.
