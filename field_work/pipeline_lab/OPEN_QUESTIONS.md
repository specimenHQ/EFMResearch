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
- Current evidence: `EV-20260902-008`.
- Next smallest observable: verify the exact EXP-003 fixture and judge, run one bounded cloud candidate, preserve raw output/cost/model metadata, then score independently.
- Resolution: open.

## Q-20260902-006
- Date opened: `2026-09-02`
- Status: `open`
- Question: Where is the authoritative current `pipeline-lab` repository/working copy, and what exact commit/state should this Microplane treat as the verified baseline?
- Why it matters: Exact experiment files and judge definitions must be read before another run; conversational reconstruction must not silently become repository truth.
- Consequence class: `operational / provenance`.
- Falsifier/weaken condition: direct access to the authoritative repository or working copy with the relevant commit and files.
- Affected decision: safe continuation and reproducibility of EXP-003.
- Current evidence: `EV-20260902-008`, `EV-20260902-009`.
- Next smallest observable: obtain the authoritative repo URL, connector access, or a mounted/exported working copy and verify `8f2adfe` plus the EXP-003 artifacts.
- Resolution: open.
