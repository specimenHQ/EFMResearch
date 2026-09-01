# Preimplementation Results — QueueGate

- A1 FALSIFIED: controlled interleaving reproduced check-closed → close transition → enqueue, allowing acceptance after close when flag check and enqueue are separate.
- A2 PASS: with `maxsize=2`, two jobs could wait while one worker simultaneously executed a third; the bound applies to waiting queue depth, not total outstanding work.
- A3 FALSIFIED naive shutdown: `put_nowait(sentinel)` raised `queue.Full` when the bounded queue was full.
- A4 PASS corrective prototype: one lock around closed-state check + admission established a single ordering point; submissions after close acquired the lock were rejected.
- A5 PASS: `Queue.join()` blocked until the worker called `task_done()` for accepted work.
- A6 PASS: 1,000 unique IDs submitted concurrently through a queue were observed exactly once in the controlled worker fixture.

Architecture earned before build: external admission lock; close marks closed under that lock, releases it, waits for accepted queued work via `join()`, then signals worker termination only after the queue is drained. Capacity claim is waiting jobs only. Evidence E2.