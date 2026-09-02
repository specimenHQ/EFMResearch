# Pipeline Lab Baseline Reconstruction — 2026-09-02

Plane-ID: `MP-PIPELINE-LAB-20260902`
Purpose: preserve only the prior state needed to continue safely. This is not a substitute for the authoritative repository.

## Source
Owner-supplied transcript of prior pipeline-lab work, pasted into the 2026-09-02 ChatGPT conversation. The owner also states that the content source involved is from a public YouTube channel.

## Reported project separation
- `EFMResearch`: canonical methodology research.
- `pipeline-lab`: applies EFM to determine what the content pipeline should be.
- future `content-pipeline`: production implementation only after `GO`.

## Reported last completed milestone
- Minimal Python + SQLite selected as orchestrator.
- Content-quality judge calibrated.
- Real analytical reference created.
- Deterministic extraction baseline killed at `1/4` recall.
- Efficiency ledger established.
- Qwen3 4B local semantic-test scaffold exercised on CPU.
- Reported Qwen boundary: CPU only, roughly four prompt tokens/second, full input exceeded context boundary, no usable output after 7m33s; model quality therefore remained untested and the local CPU path was classified `KILL`.
- Two stale documentation statements were corrected.
- Reported commit: `8f2adfe Record local semantic CPU path failure`.
- Reported worktree state after push: clean.

## Reported next direction
A one-call cloud semantic microtest against the existing EXP-003 judge was the next useful test. OpenAI API setup was blocked by reauthentication. Hermes was discussed as a possible cloud extractor route, but not justified as the pipeline orchestrator; local Hermes-scale models were considered unsuitable for the tested CPU path.

## Claim boundary
This artifact preserves the owner's supplied historical report so future work does not repeat dead ends. It does not independently prove the repository's current HEAD, worktree cleanliness, exact benchmark measurements, or the continued validity of the judge. Those must be reacquired from the authoritative project artifacts before consequential edits or a new experiment run.
