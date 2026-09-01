# Initial assumptions — pre-code inspection

| ID | Importance | Assumption | Claim scope |
|---|---|---|---|
| A1 | Operational | install failure cannot silently produce a partially valid app shell | declared precache resources |
| A2 | Operational | activation cannot delete unrelated caches | cache namespaces visible to this origin |
| A3 | Operational | fetch fallback cannot substitute an unrelated resource type/path | same-origin GET requests handled by worker |
| A4 | Operational | a new deployment cannot remain indefinitely pinned to obsolete cached shell merely because old cache entries exist | worker cache-version lifecycle |
| A5 | Architectural | behavior can be evaluated in a deterministic service-worker mock before browser integration | install/activate/fetch event logic only |

Protocol v0.2 is used unchanged. This is a prebugging study, not an EFM-native build.
