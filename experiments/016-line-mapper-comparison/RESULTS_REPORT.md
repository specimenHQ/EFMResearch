# Results Report — Experiment 016 Line Mapper Controlled Comparison

Date: 2026-08-31  
Track: build-first vs EFM controlled comparison  
Task selected randomly from five preregistered non-cyber candidates: `line_mapper`

## Experimental ordering

1. Five candidate tasks and selection method were frozen.
2. Python `secrets.choice` selected `line_mapper`.
3. The build-first implementation was written directly from the frozen requirements with no exploratory test and frozen at SHA-256 `dcf7d083b06040e241d8f894955987f732dbf166b55b0957cdcb329323ebb52f`.
4. Only after that freeze did EFM investigation begin.
5. The EFM arm recorded goal, decisions, six consequential assumptions, microtests, and a 6/6 v0.3 prebuild-completeness PASS.
6. The EFM implementation was then written and frozen, without post-build execution, at SHA-256 `e311142627d172530a2d2038152572ac8a9a4c8d3987896410931efc627ceb91`.
7. Only after both source hashes were frozen was the common evaluator authored.
8. The common evaluator rejected 5/5 known-false line mappers before either frozen candidate was evaluated.
9. Both candidates were then run against the same common evaluation.
10. After the first green checkpoint, both frozen candidates were run against the same fresh post-green challenge.

## What EFM found before implementation

EFM produced real preimplementation evidence:

- `str.splitlines(keepends=True)` is broader than the frozen task specification: it treats U+2028, NEL, vertical tab, form feed, and other characters as line boundaries;
- `splitlines` also does not itself produce the required one empty logical line for empty input or the required final empty logical line after a trailing separator;
- an explicit `\r`/`\n` scanner matched a separately implemented exact-separator regex oracle on fixed cases and 500 seeded mixed-Unicode fixtures;
- CRLF boundary semantics and Unicode code-point indexing were directly checked.

This evidence rejected a plausible convenience-API architecture before the EFM implementation was written.

However, the build-first arm had independently selected an explicit scanner directly from the requirements, so the EFM evidence did not change the final architecture relative to build-first.

## Common judge attack

Before candidate interpretation, the common evaluator rejected all five known-false implementations:

| False implementation | Failures detected |
|---|---:|
| Unicode over-splitting | 12,412 |
| LF-only separator handling | 6,984 |
| CRLF treated as two separators | 2,072 |
| trailing empty logical line omitted | 144 |
| CRLF interior offset accepted | 45 |

The common judge therefore passed its adversarial check.

## Common evaluation

The evaluator used a separately implemented exact-separator regex oracle, fixed boundary cases, Unicode cases, non-required Unicode line-break characters, 250 seeded random strings, span checks, both mapping directions, all valid-position round trips, separator-interior rejection, and basic invalid-coordinate checks.

| Metric | Build-first | EFM |
|---|---:|---:|
| Frozen-source common checks | 20,590 | 20,590 |
| Common failures | 0 | 0 |
| Rework after common evaluation | 0 | 0 |
| Implementation logical non-comment LOC | 72 | 70 |
| Third-party dependencies | 0 | 0 |
| Preimplementation EFM assumptions/microtests | 0 | 6 |
| v0.3 prebuild completeness gate | n/a | 6/6 tested |

## Post-green common challenge

A new seed (`160161`) generated 1,000 larger random mixed-Unicode/newline strings plus four deliberately structured stress fixtures. Neither frozen source was changed.

| Metric | Build-first | EFM |
|---|---:|---:|
| Post-green checks | 161,669 | 161,669 |
| Post-green failures | 0 | 0 |
| Rework | 0 | 0 |

## Evaluation-harness failure

The first candidate-run attempt failed before either candidate was scored because an ad-hoc dynamic loader did not register the EFM module in `sys.modules`, which caused Python `dataclass` processing to fail during nonstandard import. The runner was corrected; candidate sources, hashes, common evaluator, fixtures, oracle, and judge were unchanged. The corrected runner gave the results above.

This is classified as a common harness defect, not an application defect.

## Comparison result

### Delivered correctness

**Null result.** Both first implementations passed the full common evaluation and the fresh post-green challenge with zero rework.

### Architecture

**No final architecture advantage observed for EFM.** EFM experimentally rejected `splitlines` and earned an explicit scanner. Build-first independently chose an explicit scanner from the frozen requirements.

### Implementation complexity

The EFM implementation was two logical non-comment lines smaller (70 vs 72), but it also introduced a dataclass representation. This difference is too small to support a meaningful complexity claim.

### Evidence and process cost

EFM produced substantially more durable preimplementation evidence and directly demonstrated why a plausible convenience API was unsafe for the frozen semantics. Build-first produced none of that prebuild evidence, yet still delivered an equally correct first implementation.

Active time, model tokens, and dollar cost were not independently instrumented, so no numerical efficiency claim is made.

## Interpretation

Experiment 016 does **not** support a claim that EFM improves delivered correctness or reduces rework on this task. It does support the narrower claim that EFM can expose dangerous implementation alternatives before code, but that evidence may be redundant when an ordinary careful implementation already selects the correct architecture.

This is the second controlled comparison in the repository to produce a null delivered-correctness result, after experiment 001. That repeated pattern increases the importance of scope discipline: EFM should not be justified merely by the fact that it can produce more evidence; the evidence must change a consequential decision often enough to repay its process cost.

## Limitations

- Same investigator/model created both arms.
- Candidate set was investigator-designed even though task selection was randomized.
- The selected task remained finite, local, and bounded.
- No blinding beyond freezing the build-first arm before EFM exploration.
- No independent investigator reproduction; no E4 methodology claim.
- No representative operational use; no E6 claim.
- No independently instrumented time/token/cost measurement.
- One additional comparison cannot establish statistical significance.

## Research implication

More same-investigator EFM-native toy builds or similar bounded comparisons now have diminishing value. The next high-information step should seek **independent reproduction or representative real-project use** in a non-cyber domain while preserving the current evidence scale and null-result discipline.
