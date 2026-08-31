# Preimplementation Microtest Results

- **A1: PASS (E2)** — Different timestamp strings can denote the same instant; UTC normalization collapses them.
- **A2: PASS (E2)** — 8 simultaneous inserts under a PRIMARY KEY produced 1 winner and 1 stored row.
- **A3: PASS (E2)** — Forced interruption inside transaction left row counts (0, 0).
- **A4: PASS (E2)** — stdlib sqlite3 3.46.1 and datetime provide required primitives.
- **A5: PASS (E2)** — Timezone-less ISO input is distinguishable from timezone-aware input.
