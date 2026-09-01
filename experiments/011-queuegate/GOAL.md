# Goal — QueueGate

Provide a bounded in-process threaded work queue where every job reported as accepted is processed exactly once before `close()` returns, jobs not accepted are explicitly rejected, and no job can be accepted after the close transition.

Scope: one Python process, cooperative worker function, multiple producer threads, nonblocking admission, orderly shutdown. No process-crash, hostile code, distributed, or persistence claim. Protocol v0.2 unchanged; goal frozen before tests.
