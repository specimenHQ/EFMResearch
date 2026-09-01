# Outcome — Experiment 014 DAGPlan

DAGPlan is a clean Protocol-v0.3 EFM-native study in ordinary dependency planning.

## What changed before implementation

Prebuild microtests materially constrained the design:

1. mutating a live zero-indegree frontier can put a dependent in the same execution stage as its prerequisite, so each stage must snapshot the current frontier before processing;
2. exact-string lexical ordering made the plan invariant across declaration permutations;
3. duplicate task declarations must be rejected before dictionary indexing because ordinary dict construction silently overwrites them;
4. unknown dependencies must be validated before graph construction because permissive builders can silently invent undeclared nodes;
5. repeated dependency entries must be rejected because common list/set combinations can leave false residual indegree.

All six admitted consequential assumptions passed the v0.3 prebuild completeness gate before implementation.

## Integrated result

The evidence-earned implementation passed 11/11 integration tests on its first run. No application rework was required.

A nontrivial expected staging was independently checked with a recursive longest-dependency-depth oracle before acceptance. The required post-green challenge then evaluated a new six-task graph under all 720 declaration permutations; every result matched a separately derived depth oracle.

## Judge attack

The evaluator rejected 5/5 known-false planners:
- live-frontier stage collapse;
- input declaration order as tie authority;
- duplicate task last-write-wins;
- unknown dependency invention;
- silent omission of cyclic tasks.

The accepted implementation passed the evaluator.

## Interpretation

This is a non-defect EFM-native result: EFM changed several architecture and validation decisions before implementation, but the first evidence-earned implementation survived integration and post-green testing without rework.

Evidence ceiling: E5 within the finite in-memory dependency-planning scope. No distributed execution, timing/resource, E6, superiority, or cybersecurity claim is made.