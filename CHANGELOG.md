# Changelog

## 2026-08-31 — Research repository initialized

- Preserved `RESEARCH_AGENDA.md` v0.1 as the historical starting point.
- Added frozen EFM Research Protocol v0.1.
- Added Metrics v0.1 and experiment templates.
- Imported experiment 001: neutral timestamp comparison.
- Imported experiment 002: SlotLock, the first EFM-native build.
- Established separate tracks for EFM-native development and prebugging.

## 2026-08-31 — Experiment 003 MergeSafe completed

- Completed the second EFM-native build in a filesystem/data-transformation domain.
- Preserved the first green implementation as rejected v0 after judge hardening exposed two additional dangerous assumptions.
- Recorded A7 strict-JSON falsification, A8 numeric-equivalence overreach, and A9 duplicate-key silent rewrite.
- Final MergeSafe integration suite: 12/12 passing.
- Adversarial judge: 7/7 known-false implementation mutants rejected.
- Protocol v0.1 was not changed during experiment 003.

## 2026-08-31 — Protocol v0.2 adopted

- Added explicit claim-scope discipline, neighboring/boundary cases, near-miss judge attacks, and a required post-green integration challenge.
- Applied prospectively after experiment 003.

## 2026-08-31 — Research history expanded through experiment 012

- Preserved clean, null, accepted, rejected, and protocol-deviant outcomes rather than collapsing them into one success category.
- Recorded recurring evaluator false-rejection defects in experiments 006, 008, and 012.
- Recorded experiment 008 as useful evidence but excluded it from clean replication credit because admitted assumptions were tested post-hoc.
- Completed experiment 012 RowMerge as a non-cyber EFM-native CSV/data-reconciliation study at E5 within scope.

## 2026-08-31 — Protocol v0.3 adopted after experiment 012

- Added a prebuild completeness gate: every admitted consequential assumption must be tested, explicitly deferred, or removed from active scope before meaningful implementation.
- Added independent checking for nontrivial hand-derived evaluator expectations before an apparent mismatch is classified as an application defect.
- Preserved all earlier protocol versions and experiment classifications unchanged.
- Restricted active continuation to non-cyber software domains.
- Frozen v0.3 for experiments 013–015 unless a protocol-integrity defect makes continued use invalid.

## 2026-08-31 — Experiment 013 WallClock completed

- Completed the first clean Protocol-v0.3 EFM-native run in a non-cyber local scheduling/timezone domain.
- Passed the new prebuild completeness gate with 6 tested / 0 deferred / 0 removed / 0 unaccounted consequential assumptions.
- Preimplementation evidence rejected direct timezone attachment as a validity authority and rejected fixed 24-hour UTC stepping for daily local schedules across DST.
- Independently checked nontrivial evaluator expectations using fixed-offset arithmetic and UTC-to-local transition observations.
- Final integration suite: 12/12 passing.
- Post-green repeated-time range challenge: passed.
- Adversarial judge: 5/5 known-false designs rejected.
- Accepted at E5 within the tested local-scheduling scope; no E6, superiority, all-timezone, or cybersecurity claim.

## 2026-08-31 — Experiment 014 DAGPlan completed

- Completed the second clean Protocol-v0.3 run in a non-cyber dependency-planning domain.
- Passed the prebuild completeness gate with 6 tested / 0 deferred / 0 removed / 0 unaccounted consequential assumptions.
- Preimplementation evidence rejected live-frontier stage mutation and exposed duplicate-task overwrite, unknown-node invention, and duplicate-dependency accounting hazards.
- Independently checked a nontrivial expected staging with a recursive longest-dependency-depth oracle.
- Initial integration suite: 11/11 passing with no application rework.
- Post-green challenge: all 720 declaration permutations of a new six-task graph matched an independent depth oracle.
- Adversarial judge: 5/5 known-false planners rejected.
- Accepted at E5 within finite in-memory dependency-planning scope; no E6, superiority, distributed-execution, or cybersecurity claim.

## 2026-08-31 — Experiment 015 SpanEdit completed

- Completed the third clean Protocol-v0.3 run in a non-cyber Unicode text-transformation domain.
- Passed the prebuild completeness gate with 6 tested / 0 deferred / 0 removed / 0 unaccounted consequential assumptions.
- Preimplementation evidence rejected left-to-right original-coordinate mutation and confirmed same-position insertion ambiguity.
- Independently checked complex expected output using a forward-streaming reconstruction.
- Initial integration suite: 14/14 passing with no application rework.
- Post-green challenge: all 720 declaration permutations of a new Unicode/boundary fixture matched the independent streaming oracle.
- Judge v0 was rejected after an exception on a known-good case escaped the verifier; no E3 result was accepted from the defective judge.
- Corrected judge rejected 5/5 known-false editors and accepted the implementation.
- Accepted at E5 within finite in-memory Python-string editing scope; no E6, superiority, grapheme-cluster, collaborative-editing, or cybersecurity claim.

## 2026-08-31 — Protocol v0.3 review after experiment 015

- Reviewed the frozen 013–015 block.
- Found no repeated protocol-integrity defect requiring a new rule or version.
- Retained Protocol v0.3 unchanged; no v0.4 created.
- Identified research design, not protocol mechanics, as the dominant current limitation: same investigator/model, synthetic tasks, no independent E4 methodology reproduction, no operational E6 evidence, and too few direct controlled comparisons.
- Set the preferred next phase to a preregistered non-cyber build-first versus EFM comparison, preserving a null result if both arms perform equally well.

## 2026-08-31 — Experiment 016 Line Mapper controlled comparison completed

- Preregistered five non-cyber candidate tasks and randomly selected `line_mapper` using Python `secrets.choice`.
- Wrote and froze the build-first source before any exploratory or EFM testing.
- Ran the EFM arm only after build-first freeze; EFM passed the v0.3 prebuild gate 6/6 and falsified `str.splitlines()` as authority for the frozen separator semantics.
- Froze the EFM source before post-build execution.
- Authored the common evaluator only after both candidate hashes were frozen.
- Common judge rejected 5/5 known-false line mappers before candidate scoring.
- Preserved one common runner/import defect separately; candidate sources, hashes, evaluator, and oracle were unchanged by the runner correction.
- Initial common evaluation: build-first 20,590/20,590 pass; EFM 20,590/20,590 pass.
- Fresh post-green common challenge: build-first 161,669/161,669 pass; EFM 161,669/161,669 pass.
- Candidate rework: zero for both arms.
- Classified as a null delivered-correctness/rework result: EFM produced more prebuild evidence but no observed final architecture or correctness advantage.
- This is the repository's second controlled comparison with a null correctness result, reinforcing the need for scope discipline and higher-information future research rather than more same-investigator bounded trials.

## 2026-09-01 — Future-AI handoff durability phase

- Ran Fresh-Context Reconstruction Test 001 using a reduced DAGPlan packet on another AI platform.
- Preregistered threshold: 80+/100 with no critical evidence-scope failure; 90+ strong pass.
- External reconstruction scored 96/100 with zero critical failures.
- The fresh model recovered the frozen goal, A1–A6 evidence chains, E2/E3/E5 boundaries, and correctly distinguished evidence-conflicting semantic changes from an unproven DFS replacement that would require new evidence.
- External critique found that the reduced packet omitted runnable microtests, complete integration tests, independent oracle code, and judge mutants.
- Repository inspection confirmed those artifacts already existed; the defect was packaging rather than the underlying experiment record.
- Added `FUTURE_AI_HANDOFF_STANDARD.md` v0.1 as an artifact layer separate from Protocol v0.3.
- Added reusable `templates/FUTURE_AI_HANDOFF.md` and experiment-specific `experiments/014-dagplan/FUTURE_AI_HANDOFF.md`.
- Built Fresh-Context Reconstruction Test 002 with runnable prebuild microtests, implementation, integration suite, independent oracle, adversarial judge, and post-green challenge to test safe future continuation rather than prose reconstruction alone.
