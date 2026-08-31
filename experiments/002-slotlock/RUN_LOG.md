# Verification Run

## Preimplementation

- A1: PASS — Different timestamp strings can denote the same instant; UTC normalization collapses them.
- A2: PASS — 8 simultaneous inserts under a PRIMARY KEY produced 1 winner and 1 stored row.
- A3: PASS — Forced interruption inside transaction left row counts (0, 0).
- A4: PASS — stdlib sqlite3 3.46.1 and datetime provide required primitives.
- A5: PASS — Timezone-less ISO input is distinguishable from timezone-aware input.

## Final unittest suite

```text
test_cancel_by_equivalent_offset (test_slotlock.SlotLockTests.test_cancel_by_equivalent_offset) ... ok
test_concurrent_reservations_exactly_one_winner (test_slotlock.SlotLockTests.test_concurrent_reservations_exactly_one_winner) ... ok
test_equivalent_offset_double_booking_conflicts (test_slotlock.SlotLockTests.test_equivalent_offset_double_booking_conflicts) ... ok
test_equivalent_offsets_have_same_identity (test_slotlock.SlotLockTests.test_equivalent_offsets_have_same_identity) ... ok
test_internal_failure_is_not_misreported_as_conflict_and_rolls_back (test_slotlock.SlotLockTests.test_internal_failure_is_not_misreported_as_conflict_and_rolls_back) ... ok
test_naive_time_is_rejected (test_slotlock.SlotLockTests.test_naive_time_is_rejected) ... ok
test_original_input_preserved (test_slotlock.SlotLockTests.test_original_input_preserved) ... ok
test_persists_across_reopen (test_slotlock.SlotLockTests.test_persists_across_reopen) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.018s

OK
```

## Attack the judge

```text
PASS — adversarial judge rejected all 3 known-false designs
  - no storage uniqueness invariant
  - raw textual timestamp identity
  - silent naive-time acceptance
```
