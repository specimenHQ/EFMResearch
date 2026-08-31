# Decision Map — Before Code

| Area | Decision that must be earned | Consequence if wrong |
|---|---|---|
| Slot identity | What makes two timestamps the same slot? | Existential: one real instant may be double-booked |
| Exclusivity | Where is "only one reservation" enforced? | Architectural: race condition |
| Atomicity | Can a failed write leave half a reservation? | Operational: false or corrupt state |
| Time policy | What happens to timezone-less input? | Operational: silent wrong-time booking |
| Storage | What persistence mechanism is sufficient? | Architectural/optimizing |
| Dependencies | Is any external package necessary? | Optimizing |

Cosmetic CLI wording is intentionally excluded from EFM admission.
