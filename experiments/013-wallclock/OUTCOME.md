# Outcome — Experiment 013 WallClock

Status: accepted at E5 within the tested local-scheduling scope.

WallClock is the first clean EFM-native study under Protocol v0.3 and is entirely non-cyber.

## What EFM changed before implementation

Two plausible shortcuts were rejected before meaningful code:

1. attaching `ZoneInfo` directly to a requested local datetime is not a validity test; a spring-forward wall time that does not exist can still be constructed with apparent offsets;
2. adding exactly 24 hours to UTC instants does not preserve a fixed daily local wall-clock schedule across DST transitions.

The evidence-earned implementation therefore iterates local calendar dates, resolves each requested wall time independently, and accepts only fold candidates that round-trip through UTC to the exact requested local datetime. Two distinct valid UTC instants mean ambiguous; one means unique; none means nonexistent.

## Protocol v0.3 result

The new prebuild completeness gate passed before implementation: all six admitted consequential assumptions were tested, with none silently carried into the build.

Nontrivial evaluator expectations were independently checked with fixed-offset arithmetic and UTC→local transition-boundary observations before integration results were interpreted.

## Integration and judge

- final integration: 12/12 pass;
- post-green challenge: a three-day 01:30 schedule spanning the fall-back transition produced unique / ambiguous / unique classifications and four real instants while preserving the requested wall time;
- adversarial judge: 5/5 known-false designs rejected;
- third-party dependencies: none.

No post-build implementation defect was found. This is retained as a clean non-defect result in which EFM materially constrained architecture before code.

## Evidence boundary

Evidence ceiling: E5 integration for the tested `America/New_York` fixtures and the implemented standard-library classifier. No E6, superiority, all-timezone, external-calendar, or cybersecurity claim is made.
