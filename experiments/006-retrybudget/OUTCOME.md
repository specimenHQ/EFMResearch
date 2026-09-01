# Outcome — Experiment 006 RetryBudget

Status: ACCEPTED at E5.

EFM changed the design before implementation: A4 ruled out naive fixed backoff because it can cross the total deadline, and A6 prevented the project from silently claiming hard cancellation of an already-running attempt.

The first integration harness produced one false rejection from exact floating-point equality. That was an evaluator defect, not an application defect; it was corrected before results were accepted. Final integration passed 10/10, the required post-green oversleep/clock-advance challenge passed, and the adversarial judge rejected 5/5 false implementations.

No implementation defect was found after the accepted design was built. This is retained as a clean non-defect EFM-native result. No E6 or build-first superiority claim is made.
