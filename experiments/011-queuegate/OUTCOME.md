# Outcome — Experiment 011 QueueGate

Status: accepted at E5 within the frozen in-process cooperative-worker scope.

EFM changed shutdown architecture before implementation. A separate closed-flag check and enqueue was shown raceable, and an immediate sentinel could not be relied on when a bounded queue was full. The evidence-earned design uses one lock as the admission/close authority, marks the gate closed under that lock, drains all accepted queue tasks, and only then inserts worker-stop sentinels.

Final integration passed 11/11 tests. A post-green challenge repeated concurrent close-vs-submit races for 200 rounds; every reported accepted ID was processed exactly once and no post-close submission was accepted. The judge rejected 5/5 known-false designs.

No process-crash, hostile worker, persistence, distributed, or operational E6 claim.
