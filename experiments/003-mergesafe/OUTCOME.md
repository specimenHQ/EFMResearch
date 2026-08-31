# Outcome — Experiment 003 MergeSafe

Experiment 003 is the second EFM-native build and the first cross-domain replication after SlotLock.

## What EFM changed

EFM materially changed the build three times:

1. **A7 before implementation expansion:** Python's default JSON parser accepted `NaN` and infinities, so an explicit strict parse boundary was added.
2. **A8 after the first 8-test integration pass:** the initial canonicalizer falsely treated `1` and `1.0` as conflicting content, showing the original A2 microtest was too narrow. The first implementation was rejected.
3. **A9 during judge hardening:** duplicate JSON object member names were silently last-write-wins. The parser was changed to reject them.

The final architecture remained small and stdlib-only, but it is not the architecture that would have been accepted after the initial green integration suite.

## Methodological finding

This run provides evidence for two different EFM claims:

- **EFM-native design:** preimplementation falsification changed parser design before the program expanded (A7).
- **Prebugging/weak-judge defense inside an EFM-native run:** continuing past a green integration suite exposed A8 and A9, including one case where EFM's own earlier evidence had overgeneralized from an insufficient fixture.

That second result is important: EFM did not merely find application defects; it detected **false confidence produced by its own first microtest set**.

## Current status

- Final integration tests: 12/12 pass.
- Adversarial judge mutants: 7/7 rejected.
- Third-party dependencies: none.
- Evidence strength: E5 integration.
- Operational evidence: not yet established (no E6 claim).

## Limitation

MergeSafe's deterministic serializer is project-specific, not a standards claim for canonical JSON. Independent reproduction is still required before this experiment contributes E4 evidence about the methodology itself.
