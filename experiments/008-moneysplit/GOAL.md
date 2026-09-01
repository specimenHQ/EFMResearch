# Goal — MoneySplit

Allocate a nonnegative integer number of cents across recipients with nonnegative integer weights.

Required invariants: output is one integer-cent amount per input weight; allocations sum exactly to the input total; zero-weight recipients receive zero; positive-weight allocations are proportionally fair to within less than one cent of exact quota; ties are deterministic by original input order. Invalid totals/weights are rejected. No third-party dependencies unless evidence requires them.
