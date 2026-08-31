# Post-003 Protocol Review

Date: 2026-08-31
Scope: experiments 001–003

## Findings

1. **Admission/stop rule remains valid.** Experiment 001 showed full EFM can add overhead without improving outcome on a small, reversible task.
2. **Integration fault injection remains necessary.** Experiment 002 found a false conflict classification only after combining otherwise-supported pieces.
3. **Passing fixtures must not be overgeneralized.** Experiment 003's original A2 fixture passed, but later `1` vs `1.0` testing falsified the broader equivalence claim inferred from it.
4. **A green integration suite is not sufficient judge evidence.** Experiment 003 later exposed non-standard constants and duplicate-key acceptance through adversarial hardening.

## Changes earned for v0.2

- Require an explicit **claim scope** for each important microtest; evidence supports only the exercised invariant unless broader cases are separately tested.
- Require at least one **near-miss / plausible false-positive** case when attacking an important judge or classifier.
- Before assigning E5 after a green integration checkpoint, challenge at least one **integration-specific consequential failure path** not identical to the original microtest fixtures.

## Not changed

- Evidence levels.
- Assumption consequence ranking.
- EFM admission threshold.
- Stop rules.
- Requirement to preserve negative results.
- No numerical confidence weights added.

## Comparability

Experiments 001–003 remain Protocol v0.1 studies. Protocol v0.2 applies prospectively beginning with experiment 004. Results should not be silently pooled without recording protocol version.
