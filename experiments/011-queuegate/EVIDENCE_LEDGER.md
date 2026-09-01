# Evidence Ledger — Experiment 011 QueueGate

| ID | Result | Strength | Decision effect |
|---|---|---|---|
| A1 | controlled check-close-enqueue race accepted after close | E2 | closed check and admission share one lock |
| A2 | maxsize=2 allowed 2 waiting + 1 executing | E2 | capacity claim narrowed to waiting jobs |
| A3 | immediate sentinel insertion failed on full bounded queue | E2 | terminate workers only after accepted work drains |
| A4 | shared-lock prototype rejected submissions ordered after close | E2 → E5 | synchronization authority retained |
| A5 | queue join waited for task completion | E2 → E5 | close drains accepted work before worker stop |
| A6 | concurrent unique-ID fixture preserved exact set | E2 → E5 | accepted-vs-processed invariant retained |
| J1 | 5/5 known-false designs rejected | E3 | judge accepted |
| I1 | 11/11 integration + 200 close/submit race rounds pass | E5 | implementation accepted |

No process-crash, hostile-worker, persistence, distributed, or E6 claim.
