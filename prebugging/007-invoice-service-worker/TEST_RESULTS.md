# Controlled reproduction results

Frozen target: `specimenHQ/invoice:app/sw.js` blob `16f9ee32372235dabc7093ad5104a40f3b4c8ee4`.

- A1 FALSIFIED: forced `cache.addAll()` rejection is swallowed; install `waitUntil` resolves, allowing lifecycle success without completed precache.
- A2 FALSIFIED: with keys `invoice-b15`, `invoice-b16`, `other-app-cache`, activation deletes both old Invoice cache and unrelated `other-app-cache`.
- A3 FALSIFIED: offline non-navigation GET with no matching cache entry receives cached `./index.html` as fallback.
- A4 FALSIFIED: existing `invoice-b16` old index + failed `addAll` -> install resolves, activation retains current cache, offline navigation returns retained old index.

All four behaviors were reproduced in deterministic Node VM service-worker mocks against the frozen baseline source.
