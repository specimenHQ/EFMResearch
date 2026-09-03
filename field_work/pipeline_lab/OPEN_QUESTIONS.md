# Pipeline Lab Microplane Open Questions

Plane-ID: `MP-PIPELINE-LAB-20260902`
Do not delete questions; change status and preserve closure history.

## Q-20260902-005
- Date opened: `2026-09-02`
- Status: `open`
- Question: Can one inexpensive cloud semantic extractor produce output that satisfies the existing EXP-003 independent judge on the real public-source transcript?
- Why it matters: If yes, the pipeline can keep semantic extraction as a small bounded cloud stage instead of forcing inadequate deterministic extraction or oversized local inference. If no, the architecture or task decomposition may need to change.
- Consequence class: `architectural / operational`.
- Falsifier/weaken condition: a preserved cloud output that fails the existing judge on the consequential reference targets, or evidence that the judge/fixture is invalid for the task.
- Affected decision: whether a cloud semantic extractor belongs in the pipeline and which route is worth integrating.
- Current evidence: `EV-20260902-008`, `EV-20260902-011`, `EV-20260902-012`, `EV-20260902-013`.
- Next smallest observable: recover transcript text from exact video `UcBH6MCAst8`, verify it against the frozen SHA-256, then run one bounded hosted candidate using the recovered prompt and scorer; preserve raw output/cost/model metadata and score independently.
- Resolution: open.

## Q-20260902-006
- Date opened: `2026-09-02`
- Status: `answered`
- Question: Where is the authoritative current `pipeline-lab` repository/working copy, and what exact commit/state should this Microplane treat as the verified baseline?
- Why it matters: Exact experiment files and judge definitions must be read before another run; conversational reconstruction must not silently become repository truth.
- Consequence class: `operational / provenance`.
- Falsifier/weaken condition: direct access to the authoritative repository or working copy with the relevant commit and files.
- Affected decision: safe continuation and reproducibility of EXP-003.
- Current evidence: `EV-20260902-008`, `EV-20260902-009`, `EV-20260902-011`.
- Next smallest observable: none for remote continuation. If local execution/editing becomes necessary, verify the local working copy against remote `main` before using it.
- Resolution: `EV-20260902-011` verified private repository `specimenHQ/pipeline-lab`, remote `main`, and current remote commit `8f2adfe2c60c68a5ddb3a473bd5c179f7caeae8c`. Local worktree cleanliness remains unverified and is not inferred.

## Q-20260902-007
- Date opened: `2026-09-02`
- Status: `open — source locator resolved; transcript verification pending`
- Question: Can the exact public-source transcript used by the real EXP-003 calibration be reacquired and verified against frozen SHA-256 `65f4b07a2dde4881c0018bb1e23f5927bfb0013a40548b692fb665fc1150e435`?
- Why it matters: The independent scorer requires the transcript itself, and a reconstructed or different transcript could change quote fidelity and retrieval scores.
- Consequence class: `operational / provenance`.
- Falsifier/weaken condition: obtain the original transcript or a fresh transcript from the exact public source whose preserved text matches the frozen digest; if no matching source can be recovered, the fixture must be explicitly revised rather than silently substituted.
- Affected decision: whether EXP-003 can proceed as a reproducible hosted semantic microtest using the existing reference.
- Current evidence: `EV-20260902-012`, `EV-20260902-013`.
- Next smallest observable: retrieve transcript/caption text for YouTube video `UcBH6MCAst8`, preserve the raw text form, compute SHA-256 with the same UTF-8 text rule used by `verify_real_reference.py`, and compare it to the frozen digest before any hosted candidate run.
- Resolution: exact source locator is now known as `https://youtu.be/UcBH6MCAst8?si=0AZSUVQwKja3yhdu`; full transcript/digest verification remains open.
