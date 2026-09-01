# Independent Reproduction Brief — EFM

Status: ready for an external investigator/model  
Method: Evidence-First Microtesting Protocol v0.3  
Domain boundary: non-cyber software only

## Purpose

Test whether another investigator/model can apply EFM prospectively and produce independently inspectable evidence without inheriting the current repository's task outcomes or implementation choices.

This reproduction is not considered E4 merely because it is attempted. E4 methodology evidence is earned only after the submitted artifacts show meaningful independence, protocol adherence, and reproducible observations.

## Independence requirements

The reproducing investigator/model should:

1. not have participated in experiments 001–016;
2. avoid reading existing experiment outcome reports, implementation files, evidence ledgers, and interim synthesis before completing its own run;
3. receive Protocol v0.3 and this brief, but not prior conclusions about which implementation strategies worked;
4. select or receive a materially new non-cyber task independently of the current investigator;
5. preserve its own failures, false starts, evaluator defects, and protocol deviations rather than cleaning the record retrospectively.

If any independence condition cannot be met, record that limitation explicitly. Do not silently call the run independent.

## Task requirements

Choose a finite software task with at least one consequential uncertainty that could plausibly change architecture, reliability, cost, or downstream work.

Prefer a medium-consequence task rather than a trivial algorithm exercise. The task must remain outside cybersecurity. Suitable domains include ordinary data transformation, numerical/business logic, scheduling, workflow/state handling, document processing, local application behavior, or similar non-cyber software.

Before EFM work begins, freeze the task goal and scope. Do not choose a task because its expected failure mode is already known from this repository.

## Required EFM sequence

Use `PROTOCOL.md` v0.3 unchanged.

Before meaningful implementation:

1. create a durable `GOAL.md`;
2. create a `DECISION_MAP.md` identifying decisions evidence could change;
3. create an `ASSUMPTION_REGISTER.md` with consequence class, falsifier, decision effect, and claim scope;
4. run the smallest credible microtests for admitted consequential assumptions;
5. satisfy the v0.3 prebuild completeness gate: every admitted existential, architectural, and consequential operational assumption must be tested, durably deferred, or removed from scope;
6. preserve raw or inspectable preimplementation results before writing meaningful implementation code.

Then:

7. implement the smallest design supported by the evidence;
8. freeze the implementation before broad integration evaluation where practical;
9. independently check important nontrivial expected values or invariants;
10. attack the evaluator with plausible known-false or near-miss implementations before trusting it;
11. run a thin integration checkpoint;
12. after the first green checkpoint, run at least one consequential post-green challenge that is not merely a replay of the microtest fixtures;
13. preserve the final evidence ceiling honestly. Do not convert E2/E3/E5 into E6.

## Prospective instrumentation

Record these during the run rather than reconstructing them afterward when practical:

- start/end or active-work timestamps;
- time to first meaningful implementation;
- number and class of admitted assumptions;
- number of preimplementation microtests;
- implementation logical non-comment LOC;
- test/evaluator logical non-comment LOC;
- third-party dependencies introduced;
- architecture decisions changed by evidence;
- implementation discarded or materially reworked;
- consequential defects found prebuild, integration, and post-green;
- evaluator defects found;
- known-false judge cases attempted/rejected/accepted;
- evidence level reached;
- model tokens or dollar cost only if the environment can measure them reliably.

Do not invent missing timing, token, cost, or confidence numbers.

## Required submission artifacts

Submit at minimum:

- `GOAL.md`
- `DECISION_MAP.md`
- `ASSUMPTION_REGISTER.md`
- preimplementation microtest code/fixtures and raw results
- prebuild completeness record
- implementation or explicit no-build/stop decision
- independent expectation/oracle checks where applicable
- integration tests/results
- adversarial judge and judge results
- post-green challenge/results
- `EVIDENCE_LEDGER.md`
- `METRICS.md`
- `RUN_LOG.md`
- `OUTCOME.md`

The artifacts must be sufficient for another reviewer to distinguish what was believed before testing, what was observed, what changed because of evidence, and what was only learned after implementation.

## Stop and deviation rules

Stop rather than force a success if:

- an existential assumption fails;
- the requested guarantee cannot be supported within the frozen scope;
- the evaluator accepts a known falsification and cannot be repaired credibly;
- implementation would require silently narrowing the goal after observing failure.

A protocol deviation does not invalidate all observations, but the run must be labeled protocol-deviant and must not receive clean-replication credit retroactively.

## Submission review for possible E4

After the independent run is complete, a separate review should ask:

1. Was the investigator/model meaningfully independent of the prior experiments?
2. Was the task selected without using prior outcomes to engineer a favorable result?
3. Was Protocol v0.3 followed prospectively?
4. Are the claimed observations reproducible from the submitted artifacts?
5. Were evaluator failures and negative/null results preserved?
6. Did the run reproduce a methodological behavior of interest, such as evidence changing a consequential decision or detecting false confidence, rather than merely producing a correct program?

Only after that review should the repository consider whether the run contributes E4 evidence about EFM as a methodology.

## Claim boundary

One independent reproduction still would not establish universal superiority, statistical significance, known cost savings, or E6 operational support. It would be one step toward reducing the current same-investigator limitation.