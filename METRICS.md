# EFM Metrics v0.1

These measurements are descriptive. They do not yet form a single composite score, and no arbitrary numerical weights are assigned to assumption classes.

## Per experiment

Record where applicable:

- project/task identifier;
- research track (`native`, `prebugging`, `comparison`, `null`);
- start/end timestamps or elapsed active work;
- time to first meaningful implementation;
- number of assumptions admitted to EFM;
- assumption consequence classes;
- number of microtests;
- judge falsifications attempted / rejected / accepted;
- implementation logical LOC;
- test logical LOC;
- third-party dependencies introduced;
- consequential defects found before implementation expansion;
- consequential defects found at integration;
- architecture decisions changed by evidence;
- implementation discarded/reworked;
- escaped defects discovered in representative use;
- evidence level reached (E0–E6);
- whether EFM changed the final decision (`yes/no`, with explanation).

## Quantitative measures to calculate only from observed data

### Judge false-acceptance rate

`known-false cases accepted / known-false cases presented`

### Judge false-rejection rate

`known-good cases rejected / known-good cases presented`

### Consequential defect yield

`consequential defects independently reproduced / active investigation time`

Report the assumption consequence class with each defect rather than collapsing all defects into one count.

### Discovery timing

For comparable runs, record the amount of implementation already committed or constructed when a consequential assumption is first falsified. Time, LOC, dependencies, and completed integrations may all be reported; no single universal unit is assumed yet.

## Not yet permitted

Until empirical calibration exists, do not publish:

- EFM confidence percentages derived from E0–E6;
- a single universal `EFM score`;
- arbitrary numeric weights such as Existential=10, Architectural=7;
- claims of statistical significance from too few or non-independent experiments.
