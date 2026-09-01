# Evidence Ledger — Prebugging 007

| ID | Result | Strength | Consequence |
|---|---|---|---|
| A1 | falsified | E2 | failed precache can be treated as successful install |
| A2 | falsified | E2 | activation can delete unrelated same-origin caches |
| A3 | falsified | E2 | offline non-navigation requests can receive HTML shell fallback |
| A4 | falsified | E2 | failed refresh can preserve and later serve stale current-version shell |
| A5 | supported for lifecycle logic | E2 | deterministic VM mock reproduced target event logic; browser/operational behavior not claimed |
| J1 | 3/3 near-miss false workers rejected; corrected worker accepted | E3 | evaluator accepted |

No E4 independent reproduction, E5 browser integration, or E6 operational claim.
