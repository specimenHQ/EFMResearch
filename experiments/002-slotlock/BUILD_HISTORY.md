# Build History

## v0 — Rejected during EFM integration checkpoint

The first evidence-earned implementation normalized UTC identity, used SQLite
uniqueness, and wrapped reservation + event writes in a transaction.

The integration checkpoint injected a failure into the event write. Data rollback
worked, but `reserve()` caught every `sqlite3.IntegrityError` and returned `False`,
which the CLI would report as `CONFLICT`.

That was a false statement about system state: there was no competing reservation;
there was an internal write failure.

## v0.1 — Current

The smallest correction replaced broad exception classification with:

1. `INSERT OR IGNORE` only for the expected duplicate-slot reservation insert.
2. `rowcount == 0` means genuine slot conflict.
3. Subsequent event-write failures propagate normally.
4. The surrounding transaction rolls the reservation insert back.

No architecture was enlarged beyond the defect.
