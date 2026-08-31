# Evidence Ledger — Before Implementation

| Assumption | Evidence | Strength | Earned design consequence |
|---|---|---|---|
| A1 | Two unequal strings with `-06:00` and `+00:00` compared equal as datetimes | E2 | Normalize identity to UTC; preserve original separately |
| A2 | 8 simultaneous inserts under DB primary-key uniqueness produced exactly one stored row | E2 | Enforce exclusivity in storage, not check-then-insert |
| A3 | Forced exception rolled back both reservation and event writes | E2 | Keep related writes in one transaction |
| A4 | `datetime` and `sqlite3` satisfied the required primitives | E2 | No external dependencies |
| A5 | Naive timestamps are directly detectable | E2 | Reject them explicitly rather than infer a timezone |

No evidence justified a web framework, ORM, daemon, server, or GUI.
