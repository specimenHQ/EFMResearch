# EFM Neutral Pilot — Results

Date: 2026-08-31

## Question
On a small neutral programming task, does Evidence-First Microtesting (EFM) produce a better first implementation or materially better decision evidence than direct build-first development?

## Neutral task selection
Five candidate tasks were fixed before selection. Python `secrets.choice` selected `iso8601_sorter`.

Task: sort timezone-aware ISO-8601 timestamp strings by actual instant, preserve the original text, preserve caller order for equal instants, reject timezone-less timestamps, support fractional seconds, and avoid mutating input.

This task is unrelated to Aleph, AI generation, provenance, recovery, or the control plane.

## Experimental arms

### A — Build-first
The implementation was written directly from the requirements and frozen before any exploratory tests were run.

Frozen SHA-256:
`fb4be9e912994b5d29c17bfdd472a4878dab7a0e70866002da4f62f96eb5ba39`

### B — EFM
Before implementation, five assumptions were identified and microtested:

1. Lexical timestamp ordering can disagree with chronological ordering.
2. Python's parser accepts required `Z`, numeric-offset, and fractional-second forms.
3. Different textual offsets representing the same instant normalize equally.
4. Timezone-less input is detectably naive.
5. Python sorting is stable for equal keys.

All five microtests passed. This supported a standard-library implementation with no custom parser or explicit equal-instant tie-breaker.

Frozen SHA-256:
`a320faad78f29de10b64c241f3129a52df99568e765bd7c77c692711b9736a34`

## Common adversarial evaluation
Only after both implementations were frozen, a common suite was created. It included:

- a hand-checked offset/date-boundary ordering case;
- equal instants with different offsets;
- fractional seconds;
- non-mutation;
- tuple input;
- timezone-less rejection;
- a fresh 500-entry randomized fixture with offsets from UTC-12:00 through UTC+14:00 and repeated equal instants.

The randomized oracle retained the original UTC instants used to generate each text representation, so expected order did not depend on either candidate implementation's timestamp parsing.

## Results

| Metric | Build-first | EFM |
|---|---:|---:|
| Common-suite checks | 7 | 7 |
| Initial failures | 0 | 0 |
| Rework after evaluation | 0 | 0 |
| Implementation physical LOC | 15 | 13 |
| Implementation logical non-comment LOC | 11 | 9 |
| Preimplementation microtests | 0 | 5 |
| Preimplementation microtest code | 0 | 49 physical / 37 nonblank lines |
| Assumption-map artifact | none | 24 physical / 19 nonblank lines |
| New runtime dependencies | 0 | 0 |

## Attack the judge
The common evaluation suite was tested against three deliberately wrong implementations.

- Lexical sorter: 4 failures detected.
- Sorter that accepted timezone-less timestamps: 1 failure detected.
- Sorter that destroyed stable order for equal instants: 1 failure detected.

The judge therefore rejected all three known falsifications.

## Interpretation

### Delivered correctness
EFM did not improve delivered correctness in this trial. Both first implementations were correct under the common suite and required no rework.

### Implementation complexity
The EFM implementation was slightly smaller because the stable-sort microtest supported relying on Python's built-in stability rather than carrying an explicit index tie-breaker. This is a real but minor implementation difference.

### Evidence and cost
EFM produced materially more preimplementation evidence, including direct falsification of lexical ordering and confirmation that no custom or third-party timestamp parser was needed. However, the build-first arm independently selected the same basic standard-library strategy and passed every evaluation.

Therefore the extra EFM evidence did not materially change the project-level outcome on this task. Its cost was additional test and assumption-map work.

### Pilot conclusion
For this small, well-bounded task, the EFM central efficiency hypothesis is **not supported by the observed outcome**. Build-first reached an equally correct result with less process overhead.

This does not falsify EFM as a general method. It is evidence for a narrower scope rule: EFM should be concentrated on assumptions whose failure is consequential, expensive, uncertain, or likely to propagate. Applying the full method to a routine, easily reversible implementation can cost more than it saves.

## Limitations

- One task only.
- Same investigator designed and implemented both arms; no blinding.
- Candidate task selection was random from a small investigator-created set.
- Wall-clock model effort, tokens, and dollar cost were not independently instrumented, so no numeric claim is made about those metrics.
- The common judge was attacked with known falsifications, but not independently reproduced by another investigator or implementation.
- Passing this suite is evidence about this task, not operational evidence about a larger application.

## What this means for the next EFM test
The next neutral test should be a medium-consequence task with a genuinely uncertain boundary, while remaining unrelated to Aleph. The task and evaluation protocol should be preregistered before either arm is implemented. Aleph can then serve separately as the consequential real-project case study.
