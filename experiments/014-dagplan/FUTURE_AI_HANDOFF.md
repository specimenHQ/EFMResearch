# Future-AI Handoff — DAGPlan

Handoff standard: v0.1  
EFM protocol used for experiment: v0.3

## Frozen goal

Produce deterministic execution stages for a finite in-memory set of exact-string task IDs and declared dependencies. Every dependency must be in an earlier stage; same-stage tasks may run concurrently. Reject duplicate task IDs, repeated dependency entries, unknown dependencies, and cycles. Input declaration order must not change the result.

Out of scope: distributed execution, resource/timing estimation, persistence, execution engine behavior, and cybersecurity.

## Evidence-earned constraints

| Constraint | Evidence | Why it is constrained | Minimum retest if changed |
|---|---|---|---|
| Snapshot the entire current ready frontier before processing a stage | A2 | live-frontier mutation placed dependent `C` in prerequisite `A`'s stage | rerun A2 plus chain/diamond staging and post-green depth-oracle comparison |
| Deterministic stage ordering must not depend on declaration order | A3, I2 | 24 prebuild and 720 post-green permutations produced one oracle-consistent plan | rerun permutation suites with an independent expected-order authority |
| Reject duplicate task IDs before dictionary indexing | A4 | ordinary dict construction silently overwrote an earlier declaration | rerun duplicate-ID fixture and integration duplicate test |
| Validate dependency references against the complete declared-ID set before graph construction | A5 | permissive builder invented undeclared node `A` | rerun unknown-reference fixture and integration unknown-dependency test |
| Reject repeated dependency entries under the frozen goal | A6 + GOAL | mixed list/set accounting left false indegree; goal explicitly requires rejection rather than reinterpretation | changing semantics requires a new/frozen goal, then new duplicate semantics microtests and integration evidence |
| Detect cycles rather than silently omitting residual tasks | A1 + GOAL + J1 | cyclic fixture left nodes unconsumed; judge rejects silent-cycle omission | rerun two-node/self-cycle cases and judge near miss for any replacement cycle authority |

## Frozen-goal constraints

These are not merely implementation preferences. Changing them changes the project being built:

- exact-string task identity;
- declaration-order invariance;
- rejection of unknown dependencies;
- rejection of duplicate task IDs;
- rejection of repeated dependency entries;
- rejection of cycles;
- every declared task appears exactly once;
- dependency appears in an earlier stage than dependent.

A future build may intentionally choose different semantics, but it should first freeze a revised goal and then re-enter EFM. Old evidence cannot be silently relabeled as evidence for the new goal.

## Incidental implementation choices

The current evidence does **not** require these exact details so long as the frozen behavior remains true:

- exception class names and message wording;
- local variable names;
- use of lists versus other suitable internal containers for `outgoing`;
- exact function decomposition;
- the concrete Python loop structure;
- use of tuples as the returned immutable representation, unless a future caller depends on that representation as an added requirement;
- the current source-file/module layout.

Changing these does not by itself require EFM re-entry, although ordinary tests should still run.

## Unproven alternatives

### DFS/topological implementation

Status: **not falsified**.

The experiment selected Kahn-style traversal because A1 showed processed-count cycle detection works for the tested boundary and it combines naturally with frozen frontiers. That does not prove DFS is inferior or invalid.

A DFS rewrite must re-earn evidence for:

- exact stage boundaries, not merely a valid linear topological order;
- declaration-order invariance;
- cycle detection;
- duplicate/unknown input semantics;
- independent expectation/oracle agreement;
- post-green permutation invariance.

### Alternative deterministic ordering authority

Status: possible only if the frozen goal still says declaration order cannot affect the plan and the new authority is explicitly defined.

Existing A3/I2 evidence supports exact-string lexical ordering. It does not establish that lexical order is the only possible deterministic authority. A different authority would require a revised decision rule plus new oracle/permutation evidence.

## Runnable evidence inventory

- prebuild microtests: `experiments/prebuild_microtests.py`
- prebuild result interpretation: `experiments/PREIMPLEMENTATION_RESULTS.md`
- accepted implementation: `src/dagplan.py`
- integration suite: `tests/test_dagplan.py`
- integration raw result: `tests/INTEGRATION_RESULTS.txt`
- independent expectation oracle: `tests/check_expectations.py`
- oracle raw result: `tests/EXPECTATION_CHECK_RESULTS.txt`
- adversarial judge + five false planners: `tests/attack_the_judge.py`
- judge raw result: `tests/JUDGE_ATTACK_RESULTS.txt`
- post-green six-task / 720-permutation challenge: `tests/post_green.py`
- post-green raw result: `tests/POST_GREEN_RESULTS.txt`
- evidence ledger: `EVIDENCE_LEDGER.md`
- chronology: `RUN_LOG.md`
- final interpretation and claim boundary: `OUTCOME.md`

## Future-change map

| Proposed change | Classification | Existing evidence affected | Minimum action |
|---|---|---|---|
| use input declaration order inside stages | goal + evidence conflict | A3, I2 | do not adopt under current goal; otherwise revise goal and re-test determinism |
| silently deduplicate repeated dependency entries | goal conflict; old A6 no longer answers new semantics | A6 | freeze revised goal, microtest dedup semantics/accounting, rerun integration/judge |
| allow unknown dependencies as implicit tasks | goal conflict | A5 | freeze revised goal and define implicit-task semantics before new microtests |
| replace Kahn traversal with DFS | unproven / evidence does not transfer | A1, A2, A3, X1, I1, I2, J1 | re-establish stage, cycle, determinism, oracle, judge, integration, post-green evidence |
| rename exception classes | incidental / evidence-preserving if external API does not require names | none of A1–A6 | ordinary regression tests |
| change internal `outgoing` from list to another container | incidental unless it changes ordering/accounting behavior | possibly A3/A6 if semantics change | ordinary tests; re-enter EFM only if ordering/accounting becomes uncertain |
| make task IDs case-insensitive | goal conflict / new identity semantics | A3/A4 and exact-string goal | freeze new goal, microtest normalization/equivalence/duplicates/order |

## EFM re-entry triggers

Re-enter EFM when a proposed change creates consequential uncertainty about:

- identity/equivalence semantics;
- stage meaning or concurrency semantics;
- ordering authority;
- cycle authority;
- validation order when the complete task set is no longer known in advance;
- graph scale large enough that current finite small-fixture evidence no longer answers a consequential performance/resource question;
- dynamic dependencies or execution behavior, which are outside the original planner-only scope.

## Evidence ceiling

E5 within the tested finite in-memory dependency-planning scope.

No E6, distributed-execution, timing/resource, superiority, or cybersecurity claim.
