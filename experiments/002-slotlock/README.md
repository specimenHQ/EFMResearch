# SlotLock v0.1 — EFM-native build

A deliberately small stateful program built from its first decision using
Evidence-First Microtesting (EFM).

## What it does

Reserve one real instant for one person in a local SQLite file.

```bash
python src/slotlock.py --db demo.sqlite3 reserve "2026-09-01T10:00:00-06:00" Ada
python src/slotlock.py --db demo.sqlite3 reserve "2026-09-01T16:00:00+00:00" Grace
python src/slotlock.py --db demo.sqlite3 list
python src/slotlock.py --db demo.sqlite3 cancel "2026-09-01T16:00:00+00:00"
```

The second reservation reports `CONFLICT`: both timestamps identify the same instant.

## Verify

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python tests/attack_the_judge.py
```

No third-party packages are required.

## EFM trail

Read in this order:

1. `GOAL.md`
2. `DECISION_MAP.md`
3. `ASSUMPTION_REGISTER.md`
4. `experiments/PREIMPLEMENTATION_RESULTS.md`
5. `EVIDENCE_LEDGER_PREBUILD.md`
6. `history/slotlock_v0_rejected.py`
7. `BUILD_HISTORY.md`
8. `EVIDENCE_LEDGER.md`
9. `INTEGRATION_CHECKPOINT.md`

The rejected v0 is intentionally retained because EFM discovered a real error-
classification defect during integration.
