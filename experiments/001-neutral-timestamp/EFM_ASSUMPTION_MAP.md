# EFM Arm — Assumption Map

## Goal
Produce the smallest correct sorter for the written task without discovering timestamp semantics by repairing the finished implementation.

## Decision
Can Python's standard `datetime` parsing/comparison plus stable sorting satisfy the task, or is custom normalization/order logic required?

## Ranked assumptions
1. **Architectural:** timezone offsets must be compared as instants, not as timestamp text. If false/ignored, the algorithm is wrong.
2. **Architectural:** the chosen parser must accept the required `Z`, numeric offsets, and fractional seconds.
3. **Operational:** timezone-less input must be distinguishable and explicitly rejected.
4. **Operational:** equal instants written with different offsets must preserve caller order.
5. **Optimizing:** standard-library behavior is sufficient; no third-party parser is needed.

## Planned microtests
- MT1: prove a known case where lexical order disagrees with chronological order.
- MT2: verify `datetime.fromisoformat` accepts `Z`, numeric offsets, and fractional seconds on this runtime.
- MT3: verify two different-offset representations of one instant compare equal after UTC normalization.
- MT4: verify naive input is detectable (`tzinfo is None`).
- MT5: verify Python's sort is stable for equal keys.

## Stop rule
If MT1–MT5 pass, use the standard library and do not build custom timestamp parsing.
