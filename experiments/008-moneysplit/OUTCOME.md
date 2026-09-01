# Outcome — Experiment 008 MoneySplit

A1 produced a real architectural result before coding: binary-float remainder ranking can allocate cents to the wrong recipients above `2^53`, so the implementation uses exact integer quotient/remainder arithmetic.

The resulting 20-logical-LOC implementation passed 10/10 integration tests, a 10,000-case large-integer property challenge, and a judge attack rejecting 4/4 known-false implementations. One test-harness false rejection was corrected when an independent Fraction oracle showed the hand-written expected allocation was wrong.

However, A2–A6 were not microtested until after implementation. Therefore this experiment is retained as useful evidence but **not counted as a clean Protocol-v0.2 EFM-native replication**. No E6 or superiority claim is made.
