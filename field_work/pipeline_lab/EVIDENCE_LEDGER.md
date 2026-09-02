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
- Supports: this ChatGPT context cannot currently verify or modify `pipeline-lab` through the connected GitHub app.
- Does not establish: that the repository was deleted, never existed, is not private elsewhere, or that the local working copy is unavailable.
- Project consequence: do not claim exact current repo state; reacquire the authoritative source before changing experiment files.
- Conflict status: apparent tension with the historical report that a push succeeded; unresolved rather than overwritten.

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
