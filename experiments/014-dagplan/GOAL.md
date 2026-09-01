# Goal — DAGPlan

Given a finite collection of ordinary tasks identified by exact strings and their declared task dependencies, produce deterministic execution stages such that every dependency is in an earlier stage than its dependent and tasks in the same stage may run concurrently.

Requirements:
- every declared task appears exactly once in the plan;
- task identifiers are treated as exact strings;
- input declaration order must not change the plan;
- unknown dependency identifiers are rejected rather than invented;
- duplicate task identifiers are rejected;
- repeated dependency entries for one task are rejected rather than silently reinterpreted;
- dependency cycles, including self-dependency, are rejected;
- an empty task set produces an empty plan.

Scope: finite in-memory dependency graphs for local application planning. No distributed scheduling, resource estimation, timing, persistence, execution engine, or cybersecurity claim. Protocol v0.3 unchanged; goal frozen before tests.