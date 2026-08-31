# Integration Checkpoint

Verified together:

- equivalent timezone spellings collide on one canonical slot;
- 8 simultaneous reservation attempts produce exactly one winner;
- one successful reserve creates exactly one reservation event;
- persistence survives close/reopen;
- cancellation works through an equivalent offset spelling;
- an injected internal event-write failure rolls back the reservation;
- that internal failure is not mislabeled as a booking conflict;
- all three adversarial judge mutants are rejected.

Result: E5 integration evidence for this small build. No E6 operational claim.
