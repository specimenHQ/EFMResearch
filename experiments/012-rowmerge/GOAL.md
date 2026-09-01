# Goal — RowMerge

Reconcile two CSV exports by an exact record identifier and produce a deterministic report of matched, left-only, and right-only records without silently changing identifier text or discarding ambiguous rows.

Required behavior:
- identifiers are text, including leading zeros;
- quoted commas, quotes, and embedded newlines must survive CSV parsing correctly;
- duplicate identifiers in either input must be reported as ambiguity rather than silently choosing a row;
- output ordering must be deterministic;
- original row fields must remain available in the result;
- Python standard library only.

Scope: local CSV/data transformation only. This experiment does not study authentication, access control, adversarial security, network security, vulnerability discovery, or any other cybersecurity topic.

Protocol: v0.2 procedure retained unchanged for this run. Goal frozen before microtests or implementation.
