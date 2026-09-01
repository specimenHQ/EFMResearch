# Interim EFM Synthesis After Experiment 016

Date: 2026-08-31  
Status: exploratory synthesis, not a validation claim

## What the current evidence supports

### 1. EFM can change design before implementation

Across multiple EFM-native studies, controlled microtests falsified plausible assumptions early enough to alter parser choice, identity rules, transaction/error classification, timing semantics, record framing, shutdown/admission logic, timezone handling, dependency staging, and text-edit semantics.

This is the strongest repeated pattern in the repository: when a dangerous assumption is admitted explicitly and tested at the real boundary, the result can constrain implementation before the project expands.

### 2. EFM can detect false confidence in its own evidence and evaluators

The history contains cases where:
- an earlier microtest supported a claim that later proved too broad;
- a hand-written expected value was wrong;
- an adversarial judge itself was defective;
- a common runner failed before candidate scoring.

Preserving those failures matters because EFM's value cannot be evaluated only by counting application bugs found. A method that claims evidence-first development must also detect when its evidence-producing machinery is weak.

### 3. EFM does not automatically improve delivered correctness

The two controlled build-first versus EFM comparisons currently in the repository both produced null delivered-correctness results.

- Experiment 001: both first implementations passed the common adversarial evaluation with no rework.
- Experiment 016: both frozen first implementations passed 20,590 common checks plus 161,669 fresh post-green checks with no candidate failures or rework.

In both comparisons, EFM produced additional preimplementation evidence. In neither comparison did that extra evidence improve the delivered result.

This is important negative evidence against any broad claim that EFM is simply a faster or more correct way to build ordinary software.

## What the current evidence suggests, but does not prove

The emerging hypothesis is a **scope hypothesis**:

> EFM is most likely to repay its cost when a project contains a consequential, genuinely uncertain assumption whose failure can change architecture, reliability, safety, cost, or expensive downstream work.

Under this hypothesis, EFM should be selectively admitted rather than applied uniformly. Routine, bounded, easily reversible implementation details may not justify the process overhead.

The existing evidence is consistent with this hypothesis, but it is not yet strong enough to establish it generally.

## What is not supported

The repository does not currently support claims that:
- EFM is universally faster than ordinary development;
- EFM is universally more correct;
- EFM reduces total project cost by a known percentage;
- E0–E6 can be converted into confidence percentages;
- one universal EFM score is meaningful;
- the observed results are statistically significant;
- EFM has independent E4 methodology support;
- EFM has representative operational E6 support.

## Protocol assessment

Protocol v0.3 is currently adequate for continued research. Experiments 013–015 exercised its two new controls cleanly:
- the prebuild completeness gate prevented admitted consequential assumptions from being silently carried into implementation;
- independent expectation checks prevented evaluator authority from being assumed.

Experiment 015 provided direct evidence for the second control by exposing a defective judge before E3 acceptance.

No new protocol rule is justified merely because more rules could be written.

## Dominant research limitations

1. **Investigator dependence** — most studies were designed and executed by the same investigator/model.
2. **Task-selection dependence** — even randomized selections came from investigator-created candidate sets.
3. **Synthetic-task concentration** — most evidence comes from small, local, bounded software tasks.
4. **Weak cost instrumentation** — active time, model tokens, and dollar cost were not independently measured across most runs.
5. **No independent methodology reproduction** — another investigator has not yet repeated the method sufficiently independently to justify an E4 methodology claim.
6. **No representative operational use** — the repository contains no E6 methodology evidence.

## Highest-information next steps

Priority should shift away from more same-investigator toy builds.

1. **Independent reproduction**
   - another investigator/model selects or receives a non-cyber task without seeing the expected result;
   - uses Protocol v0.3 unchanged;
   - preserves all failures and deviations;
   - supplies enough artifacts for independent inspection.

2. **Representative real-project use**
   - apply EFM prospectively to a real non-cyber project before architecture is committed;
   - instrument active time and rework;
   - distinguish E2/E3 prebuild evidence from E5 integration and eventual E6 use.

3. **Better comparative instrumentation**
   - if more build-first comparisons are run, record active work time, implementation/test LOC, rework, and decision changes prospectively rather than reconstructing cost afterward.

## Current research posture

EFM remains a viable exploratory method with repeated evidence that it can expose consequential assumptions and evaluator weakness before expensive expansion. The controlled null results materially limit the stronger claim: more evidence does not automatically mean a better delivered implementation.

The next credible advance requires **independence or operational representativeness**, not another internally generated success case.
