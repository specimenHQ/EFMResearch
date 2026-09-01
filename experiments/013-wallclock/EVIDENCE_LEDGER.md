# Evidence Ledger — Experiment 013 WallClock

Protocol: v0.3

| ID | Evidence | Strength | Decision effect |
|---|---|---|---|
| A1 | nonexistent `2026-03-08 02:30` accepted by direct attachment but neither fold round-tripped | E2 | direct timezone attachment rejected as validity authority |
| A2 | fall-back `2026-11-01 01:30` produced two valid folds at `05:30` and `06:30 UTC` | E2 | retain fold-aware representation |
| A3 | round-trip classifier separated controlled unique, nonexistent, and ambiguous fixtures | E2 → E5 | classifier retained |
| A4 | fixed 24-hour UTC stepping shifted local 09:00 to 10:00/08:00 across DST changes | E2 | iterate local calendar dates, resolve each independently |
| A5 | distinct-valid-UTC criterion separated ordinary, gap, and repeat cases | E2 → E5 | ambiguity requires two valid distinct instants |
| A6 | `America/New_York` loaded through stdlib `zoneinfo` | E2 | no dependency added |
| V1 | fixed-offset arithmetic and UTC transition-boundary observations independently checked important expected values | evaluator check | integration expectations accepted |
| J1 | 5/5 known-false designs rejected; accepted implementation accepted | E3 | evaluator accepted |
| I1 | 12/12 integration including post-green repeated-time range | E5 | implementation accepted within tested scope |

No E6 operational evidence is claimed.
