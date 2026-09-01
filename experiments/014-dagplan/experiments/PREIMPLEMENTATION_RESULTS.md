# Preimplementation Results — DAGPlan

Protocol: v0.3

All admitted consequential assumptions A1–A6 were exercised before implementation.

- **A1 PASS / E2:** Kahn-style traversal consumed all nodes in a controlled acyclic chain and consumed none of a two-node cycle. Decision: retain processed-count cycle detection after validation.
- **A2 FALSIFIED naive staging / E2:** a live, mutating zero-indegree frontier placed `C` in the same stage as prerequisite `A` for graph `A -> C` with independent `B`. Freezing the frontier produced `[[A,B],[C]]`. Decision: stage frontier must be snapshotted before processing.
- **A3 PASS / E2:** all 24 declaration permutations of a four-task fixture produced the identical staged plan `[[A,B],[C],[D]]` when each frontier was exact-string sorted. Decision: lexical frontier ordering is the deterministic authority.
- **A4 CONFIRMED hazard / E2:** ordinary dictionary construction silently overwrote the first of two `A` task declarations. Decision: detect duplicate task IDs before indexing.
- **A5 CONFIRMED hazard / E2:** permissive `setdefault` graph construction invented undeclared dependency `A` when only task `B` was declared. Decision: validate all dependency references against the complete declared-ID set before graph construction.
- **A6 CONFIRMED hazard / E2:** counting duplicate dependency entries in indegree while deduplicating adjacency left task `B` with false residual indegree 1. Decision: reject repeated dependency entries explicitly before planning.

Neighbor fixtures exercised prebuild: independent tasks, a chain, a dependency-level boundary, declaration permutations, two-node cycle, duplicate task ID, unknown dependency, and duplicate dependency entry. Empty graph, diamond, and self-cycle remain required integration cases.

## v0.3 prebuild completeness gate

| Assumption | Status before implementation |
|---|---|
| A1 | tested E2 |
| A2 | tested E2 |
| A3 | tested E2 |
| A4 | tested E2 |
| A5 | tested E2 |
| A6 | tested E2 |

Gate result: **PASS — 6/6 admitted consequential assumptions dispositioned before implementation.**
