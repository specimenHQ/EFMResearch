# MergeSafe — EFM-native build #003

MergeSafe merges JSON Lines records by `id` while refusing silent conflicts and protecting a previous valid output from failed merges.

This experiment was built under the frozen EFM Research Protocol v0.1.

## Verify

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python tests/attack_the_judge.py
python experiments/efm_008_009_equivalence_and_duplicate_keys.py
```

## Evidence trail

1. `GOAL.md`
2. `DECISION_MAP.md`
3. `ASSUMPTION_REGISTER.md`
4. `experiments/PREBUILD_RESULTS.txt`
5. `experiments/A7_RESULTS.txt`
6. `EVIDENCE_LEDGER_PREBUILD.md`
7. `history/mergesafe_v0_rejected.py`
8. `experiments/A8_A9_RESULTS.txt`
9. `BUILD_HISTORY.md`
10. `EVIDENCE_LEDGER.md`
11. `INTEGRATION_CHECKPOINT.md`
12. `METRICS.md`
13. `OUTCOME.md`

The rejected v0 is retained because the first green integration suite was not sufficient: later EFM judge hardening exposed an architectural equivalence error and silent duplicate-member rewriting.
