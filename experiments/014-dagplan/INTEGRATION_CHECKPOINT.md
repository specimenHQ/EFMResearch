# Integration Checkpoint — DAGPlan

Protocol: v0.3

## Initial integration

- 11 tests run.
- 11 passed.
- 0 failed.
- No application rework required.

Covered: empty graph, independent tasks, chain, diamond, declaration-order invariance, duplicate task rejection, unknown dependency rejection, duplicate dependency rejection, two-node cycle, self-cycle, and exact case-sensitive string identity.

## Independent expectation check

Before accepting the nontrivial staged expectation for a five-task graph, a separate recursive longest-dependency-depth oracle derived `((A,B),(C,D),(E))`. It matched the expected plan without reusing DAGPlan's Kahn traversal.

## Required post-green challenge

A new six-task graph with cross-layer dependencies was evaluated under all 720 declaration permutations. A separate recursive depth oracle derived `((A,C),(B,D),(E),(F))`; every permutation produced that plan.

No emergent integration defect was found after the first green suite. Evidence ceiling: E5 within the finite in-memory task-planning scope.