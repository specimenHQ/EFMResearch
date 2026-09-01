# Outcome — Prebugging 007 Invoice service worker

Status: four reproducible operational defects/risks found in the frozen existing implementation; Invoice repository left unchanged.

1. Install suppresses precache failure, so the worker can activate without proving the app shell was cached.
2. Activate deletes every cache except the current Invoice cache, including unrelated caches sharing the origin.
3. Offline fallback returns `index.html` for arbitrary uncached GETs rather than only navigation requests.
4. Combined with swallowed install failure, an existing current-version cache can survive a failed refresh and later serve stale shell content offline.

The evaluator rejected 3/3 near-miss false workers and accepted a corrected worker. Evidence is E2/E3 only: no browser integration, independent reproduction, or operational-use claim yet.
