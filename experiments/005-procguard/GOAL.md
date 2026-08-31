# Goal — ProcGuard exploratory run

Run a local POSIX command with a hard timeout, capture stdout/stderr, distinguish success/nonzero/signal/timeout, and ensure timeout does not leave child or grandchild work running.

Protocol note: this goal was not durably committed before the first microtest. Therefore experiment 005 is retained as exploratory/protocol-deviant evidence and is not counted as a clean v0.2 replication.
