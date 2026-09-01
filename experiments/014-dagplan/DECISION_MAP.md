# Decision Map — DAGPlan

Protocol: v0.3

## Decisions that evidence can change

1. **Planning algorithm**
   - Candidate: Kahn-style indegree traversal.
   - Alternative: recursive DFS/topological ordering.
   - Evidence needed: reliable cycle detection and deterministic stage construction.

2. **Stage construction**
   - Candidate: process the entire current zero-indegree frontier as one stage, then discover the next frontier.
   - Risk: allowing newly-ready tasks into the current frontier can collapse dependency levels incorrectly.

3. **Input validation authority**
   - Unknown dependencies, duplicate task IDs, and duplicate dependency entries must be resolved before planning.
   - Risk: dictionary/set convenience can silently overwrite, invent, or reinterpret input.

4. **Determinism rule**
   - Candidate: exact-string lexical ordering inside each frontier.
   - Evidence needed: plan must remain identical across task declaration permutations.

5. **Dependencies representation**
   - Candidate: validated unique dependency sets after duplicate-entry rejection.
   - No normalization of task identifiers beyond exact string identity.

No implementation architecture beyond these candidate decisions is accepted before the prebuild completeness gate passes.