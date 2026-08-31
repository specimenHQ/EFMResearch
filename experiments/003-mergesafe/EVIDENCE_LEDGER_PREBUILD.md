# Evidence Ledger — Before Implementation

| Assumption | Result | Strength | Earned consequence |
|---|---|---|---|
| A1 raw text is unsafe equivalence | Two unequal JSON strings parsed to equal objects | E2 | Compare parsed values, not source text |
| A2 stdlib canonical representation | Chosen sorted-key/fixed-separator serialization produced identical bytes for equivalent objects | E2 | Use canonical JSON for deterministic output and duplicate comparison |
| A3 staged output commit | Injected failure before `os.replace` left old output unchanged | E2 | Write/flush/fsync temp file in destination directory, replace only after success |
| A4 path alias detection | `os.path.samefile` identified a symlink alias | E2 | Reject an existing output path that is the same file as any input |
| A5 deterministic rendering | Reordered inputs and object keys yielded identical bytes | E2 | Sort by `id` and serialize canonically |
| A6 stdlib sufficiency | Required boundary mechanisms exist in Python stdlib | E2 | No third-party dependency justified |

All existential, architectural, and admitted operational assumptions have controlled evidence. The stopping rule therefore permits the smallest implementation consistent with these constraints.

## New assumption discovered before implementation expansion

| Assumption | Result | Strength | Earned consequence |
|---|---|---|---|
| A7 default parser is strict JSON | **FALSIFIED:** default `json.loads` accepted `NaN`, `Infinity`, and `-Infinity`; an explicit `parse_constant` hook rejected all three | E2 | Parser must explicitly reject non-standard numeric constants |

This is the first decision-changing falsification in build #003. It was discovered after the initial assumption map but before meaningful implementation, so the protocol required returning from build planning to microtesting rather than silently absorbing the behavior.
