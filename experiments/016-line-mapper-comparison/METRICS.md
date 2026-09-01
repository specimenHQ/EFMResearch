# Metrics — Experiment 016 Line Mapper Controlled Comparison

## Build-first arm

- track: controlled comparison / build-first
- source written before exploratory testing: yes
- frozen SHA-256: `dcf7d083b06040e241d8f894955987f732dbf166b55b0957cdcb329323ebb52f`
- implementation logical non-comment LOC: 72
- preimplementation microtests: 0
- third-party dependencies: 0
- initial common evaluation: 20,590 pass / 0 fail
- post-green common challenge: 161,669 pass / 0 fail
- application rework: 0

## EFM arm

- track: controlled comparison / EFM
- protocol: v0.3
- build-first source frozen before EFM exploration: yes
- admitted consequential assumptions: 6
- prebuild completeness: 6 tested / 0 deferred / 0 removed / 0 unaccounted
- frozen SHA-256: `e311142627d172530a2d2038152572ac8a9a4c8d3987896410931efc627ceb91`
- implementation logical non-comment LOC: 70
- third-party dependencies: 0
- initial common evaluation: 20,590 pass / 0 fail
- post-green common challenge: 161,669 pass / 0 fail
- application rework: 0
- EFM changed a preimplementation decision: yes — `splitlines` rejected as segmentation authority
- EFM changed final architecture relative to build-first: no

## Common evaluator

- authored after both candidates frozen: yes
- known-false implementations: 5 presented / 5 rejected / 0 accepted
- runner defects: 1, corrected before candidate scoring
- common oracle: exact `\r\n|\r|\n` regex segmentation + mapping invariants

## Comparative outcome

- delivered-correctness advantage: none observed
- rework advantage: none observed
- implementation-size advantage: 2 logical lines in EFM arm; not treated as meaningful
- EFM process/evidence overhead: present and not independently time/token/cost instrumented
- evidence level for frozen candidate behavior: E5-style common integration evidence
- methodology reproduction level: not E4; same investigator/model
- operational evidence: none / no E6 claim
