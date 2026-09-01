# Protocol Review After Experiment 012

Date: 2026-08-31
Scope: evidence recorded through experiment 012

## Purpose

Review Protocol v0.2 after its original freeze window and decide whether observed research-process failures justify a prospective revision. Earlier experiments are not reclassified by this review.

## Evidence considered

### Experiment 006 — RetryBudget

The accepted implementation reached E5, but the first integration harness falsely rejected it because the evaluator used exact floating-point equality. The evaluator was corrected before the result was accepted.

### Experiment 008 — MoneySplit

A1 changed numeric architecture before implementation, but A2–A6 were not microtested until after implementation. The run was therefore retained as useful evidence but excluded from clean Protocol-v0.2 EFM-native replication credit. The integration harness also produced a false rejection from an incorrect hand-written expected allocation; an independent `fractions.Fraction` oracle corrected it.

### Experiment 010 — RecordTape

Preimplementation testing changed framing architecture before implementation, and the resulting implementation passed integration, post-green, and judge challenges. No protocol-integrity defect was recorded.

### Experiment 011 — QueueGate

Preimplementation concurrency evidence changed shutdown architecture before implementation. Integration and post-green race testing passed; no protocol-integrity defect was recorded.

### Experiment 012 — RowMerge

Preimplementation evidence changed identity, duplicate, invalid-row, and ordering rules before implementation. The first integration run produced one false rejection because the evaluator contained an incorrect hand-written Unicode sort expectation. Correcting the evaluator required no application change.

## Repeated methodological findings

Two failures now recur often enough to justify protocol hardening.

1. **Prebuild completeness can be ambiguous.** Merely freezing an assumption register is insufficient if implementation begins before every admitted consequential assumption is either tested, explicitly deferred, or explicitly removed from the active claim scope. Experiment 008 demonstrated this failure directly.

2. **The evaluator itself can generate consequential false negatives.** Experiments 006, 008, and 012 each contained an evaluator error that initially looked like an application failure. Protocol v0.2 requires attacks with known-false candidates, but it does not explicitly require an independent check of nontrivial expected values before blaming the candidate implementation.

## Decision

Adopt Protocol v0.3 prospectively beginning with experiment 013.

The revision should add only two requirements:

- a **prebuild completeness gate**: before meaningful implementation, each admitted existential, architectural, and consequential operational assumption must be marked `tested`, `deferred with reason`, or `removed from active scope`; a clean EFM-native replication cannot receive that label if implementation begins with unaccounted admitted assumptions;
- an **evaluator expectation check**: when an important expected result is nontrivial or hand-derived, validate it with an independent derivation, invariant, alternate oracle, or neighboring known-good case before treating a mismatch as an application defect.

No numerical confidence system, composite EFM score, extra framework, or new evidence level is added.

## Comparability

- Experiments 001–003 remain Protocol v0.1 studies.
- Experiments 004 onward that were explicitly run under v0.2 remain v0.2 studies with their original clean/deviant classifications preserved.
- Protocol v0.3 applies only to experiment 013 and later.

## Current research boundary

Active continuation is restricted to non-cyber software domains. Historical repository material is preserved, but new experiments will not study cybersecurity, exploitability, access control, attack surfaces, or related security questions.
