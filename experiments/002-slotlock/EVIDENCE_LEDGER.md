# Evidence Ledger — Current

| Item | Evidence | Strength | Current conclusion |
|---|---|---|---|
| A1 time identity | Controlled equivalent-offset experiment + integration test | E5 | UTC-normalized canonical slot identity survives integration |
| A2 exclusivity | 8-way concurrent microtest + 8-way final integration test | E5 | DB uniqueness permits exactly one winner |
| A3 atomicity | Forced prebuild rollback + forced event-write failure in final system | E5 | Reservation and audit event remain atomic |
| A4 stdlib sufficiency | Complete working implementation, no third-party imports | E5 | External dependency not justified |
| A5 naive-time policy | Controlled detection + final rejection test | E5 | No silent timezone guessing |
| J1 measuring instrument | Three deliberately false designs are rejected | E3 | Judge is not merely accepting expected labels |
| F1 error classification | v0 returned `False/CONFLICT` for an internal event failure | E2 defect observation | Broad IntegrityError catch rejected |
| F1 correction | v0.1 propagates internal IntegrityError while rolling reservation back | E5 | Expected conflict and internal failure are now distinguishable |

E5 here means the evidence survived interaction inside this small integrated program.
It does not claim E6 representative operational use.
