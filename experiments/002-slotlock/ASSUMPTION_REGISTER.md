# Assumption Register — Initial State

| ID | Importance | Assumption | Before test |
|---|---|---|---|
| A1 | Existential | Raw timestamp strings are not safe identities because different offsets may name the same instant | E0 |
| A2 | Architectural | Database uniqueness can arbitrate simultaneous reservations more safely than application check-then-insert | E0 |
| A3 | Operational | A transaction can prevent a deliberately interrupted multi-write reservation from persisting partial state | E0 |
| A4 | Optimizing | Python stdlib provides sufficient time and durable storage primitives | E0 |
| A5 | Operational | Timezone-less ISO input is detectable and can be rejected rather than guessed | E0 |

Stopping rule: if A1–A5 are supported and no new dangerous assumption appears,
build the smallest implementation implied by the evidence.
