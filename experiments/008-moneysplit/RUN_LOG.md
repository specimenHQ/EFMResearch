# Run Log — Experiment 008

1. Goal, decision map, assumptions, and claim scopes committed before tests (`8931820c24274032deb4214ea374b071b3ddd3a8`).
2. A1 microtest found a float-ranking counterexample and changed numeric architecture to exact integer arithmetic.
3. Implementation was written before A2–A6 were separately microtested. This is recorded as a protocol deviation, not repaired retroactively.
4. First integration run had one false rejection from an incorrect hand expected value; independent Fraction oracle corrected the judge. No application code changed.
5. Final integration 10/10 pass.
6. Post-green 10,000 randomized large-integer invariant cases pass.
7. Judge attack rejected 4/4 known-false implementations and accepted current implementation.
8. A2–A6 post-hoc probes pass; study remains excluded from clean replication count.
