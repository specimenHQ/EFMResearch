# Evidence Ledger — Final for Experiment 003

| Item | Evidence | Strength | Current conclusion |
|---|---|---|---|
| A1 raw text equivalence | Unequal source JSON with key/whitespace differences parsed to the same value; final integration collapses them | E5 | Raw source text is not record equivalence |
| A2 initial stdlib canonicalizer | Initial key-order fixture passed, but A8 later falsified the broader equivalence claim | **Superseded** | The first A2 evidence was too narrow |
| A3 staged output commit | Prebuild injected failure + final mocked `os.replace` failure preserve old output and clean temp | E5 | Replace-after-complete protocol survives integration |
| A4 path alias detection | `samefile` microtest + final symlink-output integration test | E5 | Existing output aliases of inputs are rejected |
| A5 deterministic output | Reordered inputs/key order in microtest and final integrated build produce byte-identical output | E5 | Output is deterministic for accepted records |
| A6 stdlib sufficiency | Final implementation uses only Python stdlib, including `decimal` | E5 | No external dependency is currently justified |
| A7 strict numeric constants | Default parser accepted `NaN`/`Infinity`; explicit rejection was microtested and integrated | E5 | Non-standard constants are rejected |
| A8 numeric equivalence | Rejected v0 falsely conflicted on `1` vs `1.0`; v0.1 lossless number parsing + canonical number rendering collapses them; large exponent and bool-vs-number guards pass | E5 | Numeric spellings no longer create false conflicts while JSON types remain distinct |
| A9 duplicate object members | Rejected v0 silently used last-write-wins; v0.1 rejects duplicate names and preserves previous output | E5 | Duplicate member names cannot silently rewrite a record |
| J1 judge | Known-good baseline accepted; 7 deliberately false implementation mutants rejected | E3 | Current judge demonstrated discrimination against seven targeted falsifications |

No E6 claim is made. Representative operational use has not occurred.
