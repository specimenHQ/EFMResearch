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
