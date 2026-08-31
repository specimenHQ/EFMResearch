# Experiment Record — 003 MergeSafe

## Identity

- Date: 2026-08-31
- Research track: `native`
- Protocol: `EFM Research Protocol v0.1`
- Protocol status: frozen; unchanged during this build
- Domain: local filesystem / structured data transformation
- Previous EFM-native build: 002 SlotLock (stateful reservation / concurrency / time identity)
- Deliberate domain change: no time identity, reservation logic, or concurrent booking behavior

## Durable goal

Merge JSONL record files into one deterministic artifact without silently losing or rewriting conflicting records, and preserve the previous valid output whenever a merge fails.

## Decision sequence

The run began with six ranked assumptions. All received E2 controlled evidence. During implementation planning, A7 was discovered and falsified, changing the parser before meaningful implementation.

The first integrated implementation then passed 8/8 tests. The protocol did not permit closure because the judge had not been adversarially attacked. Judge hardening exposed A8 and A9, forcing the first implementation to be rejected and revised.

## Decision-changing falsifications

- A7: default JSON parsing accepts non-standard `NaN`/`Infinity` constants.
- A8: initial canonical rendering did not preserve parsed-value numeric equivalence (`1` vs `1.0`).
- A9: default object parsing silently overwrites duplicate object member names.

## Final result

- Final integration: 12/12 tests passing.
- Judge: 7/7 known-false implementation mutants rejected.
- Dependencies: Python standard library only.
- Evidence: E5 integration; no E6 claim.
- EFM changed final implementation: yes.

## Negative/self-critical result

The initial A2 controlled microtest was too narrow. It established key-order/whitespace canonicalization but not the broader equivalence claim later inferred from it. A8 exposed that overreach. This is retained as evidence of a failure mode in EFM itself: a microtest can create false confidence when its fixture is not representative of the invariant being claimed.
