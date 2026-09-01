# Evidence Ledger — Experiment 014 DAGPlan

Protocol: v0.3

| ID | Evidence | Strength | Decision effect |
|---|---|---|---|
| A1 | controlled acyclic chain consumed all nodes; two-node cycle left nodes unconsumed | E2 | retain processed-count cycle detection after validation |
| A2 | live frontier collapsed `A -> C` into one stage; frozen frontier produced `[[A,B],[C]]` | E2 | snapshot each ready frontier before processing |
| A3 | 24 declaration permutations produced one exact staged plan | E2 | exact-string lexical ordering is deterministic authority |
| A4 | ordinary dict construction overwrote duplicate task `A` | E2 | reject duplicate task IDs before indexing |
| A5 | permissive graph builder invented undeclared dependency `A` | E2 | validate all references against complete declared-ID set first |
| A6 | duplicate dependency plus mixed list/set accounting left false indegree 1 | E2 | reject repeated dependency entries before planning |
| X1 | independently derived longest-dependency-depth oracle matched nontrivial expected staging | E2 independent expectation check | evaluator expectation accepted |
| J1 | 5/5 known-false planners rejected; accepted implementation accepted | E3 | evaluator accepted |
| I1 | 11/11 integration tests passed without application rework | E5 | implementation accepted within scope |
| I2 | 720 declaration permutations of new six-task graph matched independent depth oracle | E5 post-green | deterministic staging claim retained |

Prebuild completeness: 6/6 admitted consequential assumptions tested before implementation. No E6 claim.