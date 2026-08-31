# Outcome — Experiment 005 ProcGuard

Status: STOP / no accepted implementation.

Findings:
1. Prebuild A1 falsified the naive assumption that `subprocess.run(timeout=...)` cleans up descendants: the direct child timed out while its grandchild remained alive.
2. That evidence changed the first implementation to `start_new_session=True` plus process-group SIGKILL.
3. Initial integration then passed 10/10 tests, including ordinary nested descendants.
4. Post-green challenge used a descendant that created its own session. A requested 0.4 s timeout returned after 3.020 s because the detached descendant escaped the killed group and retained inherited output pipes.

Conclusion: a simple stdlib process-group wrapper cannot support the broad hard-timeout/no-surviving-descendants guarantee against descendants that deliberately detach. The build is stopped rather than narrowing the goal after observing the failure.

Research qualification: the durable pre-code goal/assumption artifacts were not frozen before execution, so this study is useful evidence but not a clean protocol-v0.2 replication.
