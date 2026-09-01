# Protocol Review After Experiment 015

Date: 2026-08-31  
Protocol reviewed: v0.3 — Prebuild completeness and evaluator integrity

## Review question

Did experiments 013–015 reveal a protocol-integrity defect or repeated methodological failure that justifies changing v0.3 before the next research phase?

## Evidence from the frozen v0.3 block

### 013 — WallClock

- clean EFM-native run;
- 6/6 admitted consequential assumptions tested before implementation;
- two plausible architecture shortcuts rejected before code;
- nontrivial evaluator expectations independently checked;
- first evidence-earned implementation passed 12/12 integration and post-green challenge without rework;
- judge rejected 5/5 known-false designs;
- E5 only.

### 014 — DAGPlan

- clean EFM-native run;
- 6/6 admitted consequential assumptions tested before implementation;
- live-frontier staging and several permissive input shortcuts rejected before code;
- nontrivial expected staging independently derived with a different algorithm;
- first evidence-earned implementation passed 11/11 integration and a 720-permutation post-green challenge without rework;
- judge rejected 5/5 known-false planners;
- E5 only.

### 015 — SpanEdit

- clean EFM-native run;
- 6/6 admitted consequential assumptions tested before implementation;
- left-to-right mutation and ambiguous insertion semantics rejected before code;
- nontrivial output independently derived with a forward-streaming oracle;
- first evidence-earned implementation passed 14/14 integration and a 720-permutation Unicode/boundary challenge without rework;
- first adversarial judge was itself defective and was rejected before E3 acceptance;
- corrected judge rejected 5/5 known-false editors;
- E5 only.

## Findings

### 1. The prebuild completeness gate worked as intended

Across all three clean v0.3 runs, every admitted consequential assumption was dispositioned before meaningful implementation. No repeat of experiment 008's post-hoc assumption-testing deviation occurred.

### 2. Independent expectation checks were useful rather than ceremonial

Experiments 013 and 014 used alternate calculations/algorithms to validate nontrivial expected results. Experiment 015 additionally showed why evaluator integrity matters: the first judge contained a real control-flow defect and was rejected before its result could be treated as evidence.

### 3. No new protocol failure repeated across the block

No observation from 013–015 requires a new step, evidence level, scoring system, or assumption class. Adding another rule now would be protocol growth without a demonstrated need.

### 4. The dominant limitation has moved from protocol mechanics to research design

The evidence base is still constrained by:

- one investigator/model conducting the studies;
- investigator-designed synthetic tasks;
- no independent reproduction sufficient for E4 methodology evidence;
- no operational E6 evidence;
- few direct comparisons against a frozen ordinary-development arm;
- no basis for statistical significance or a universal EFM score.

More EFM-native toy builds alone would now have diminishing information value.

## Decision

**Retain Protocol v0.3 unchanged. Do not create v0.4.**

No protocol-integrity defect was observed in the frozen 013–015 block. Earlier protocol history and experiment classifications remain unchanged.

## Next research phase

The next experiment should change the research design rather than the method. Preferred next step:

1. run a preregistered, non-cyber controlled comparison on a medium-consequence task with a genuinely uncertain boundary;
2. write and freeze the build-first implementation before any EFM microtests are run;
3. then run the EFM arm under unchanged v0.3;
4. freeze both implementations before creating the common adversarial evaluation;
5. attack the common judge with known-false implementations;
6. compare delivered correctness, rework, architecture decisions, implementation size, test/process overhead, and evidence produced;
7. preserve a null result if build-first performs equally well.

A later independent reproduction by another investigator or implementation remains necessary before claiming E4 support for the methodology.

Active continuation remains restricted to non-cyber software domains.