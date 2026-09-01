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
