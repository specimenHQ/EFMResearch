# Assumption Register — QueueGate

| ID | Class | Assumption | Claim scope |
|---|---|---|---|
| A1 | Architectural | checking a closed flag separately from enqueue can race with close | controlled producer/close interleaving |
| A2 | Operational | `queue.Queue(maxsize=N)` bounds waiting queued jobs, not currently executing work | one worker plus bounded queue |
| A3 | Architectural | inserting a shutdown sentinel immediately can fail or reorder shutdown when the bounded queue is full | nonblocking admission, bounded queue |
| A4 | Operational | marking closed under the same lock used for admission gives a linearizable no-new-acceptance boundary | same-process producer threads |
| A5 | Operational | waiting for queue task completion before worker termination preserves all accepted work | cooperative workers using `task_done` correctly |
| A6 | Operational | accepted job IDs can be compared with processed IDs to detect loss or duplication under concurrent producers | unique immutable test job IDs |

Neighbor cases: full queue, empty queue, close during submit, repeated close, worker already processing while close starts, concurrent producers with rejections.
