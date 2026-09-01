# Assumption Register — DAGPlan

Protocol: v0.3

| ID | Class | Assumption | Claim scope | Falsifier / decision effect |
|---|---|---|---|---|
| A1 | Architectural | Kahn-style indegree traversal can detect a cycle by failing to consume every declared task | finite directed task graph after validation | a cyclic graph consumes every node or an acyclic graph is falsely rejected; change algorithm |
| A2 | Architectural | freezing the current zero-indegree frontier before processing it produces correct dependency stages | graphs where newly-ready nodes depend on current-stage nodes | a dependent enters the same stage as one of its prerequisites; change stage construction |
| A3 | Operational | exact-string lexical ordering of each frontier makes the staged plan invariant to input declaration order | same graph under materially different declaration permutations | permutations produce different plans; change deterministic authority |
| A4 | Operational | dictionary indexing by task ID can silently destroy duplicate task declarations | repeated exact task IDs | duplicate declarations survive ordinary dict construction as if valid; validation strategy changes |
| A5 | Operational | permissive graph construction can silently invent an unknown dependency as a graph node | dependency references absent from declared tasks | unknown reference cannot be made to appear as a node under a plausible builder; validation priority changes |
| A6 | Operational | duplicate dependency entries can corrupt indegree accounting or be silently reinterpreted by common list/set combinations | one task listing the same dependency more than once | duplicate entries cannot produce inconsistent graph accounting; duplicate rejection may be unnecessary |

Prebuild completeness requirement: A1–A6 must each be tested, deferred with a durable reason, or removed from scope before meaningful implementation begins.

Neighbor cases required before implementation: empty graph, independent tasks, one chain, diamond dependency, declaration-order permutation, two-node cycle, self-cycle, duplicate task ID, unknown dependency, duplicate dependency entry.