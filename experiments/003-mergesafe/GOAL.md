# MergeSafe — Durable Goal

Build a small local tool that merges JSON Lines (`.jsonl`) record files into one deterministic output without silently losing or rewriting conflicting records.

The durable outcome is:

> A merge either produces one complete, deterministic result consistent with all accepted inputs, or leaves the previous output unchanged.

Required behavior:

- every nonblank input line must be a JSON object with a nonempty string `id`;
- repeated records with the same `id` and equivalent JSON content may collapse to one record;
- repeated `id` values with materially different content must stop the merge rather than choose a winner;
- malformed input must stop the merge with source/line context;
- output order must be deterministic;
- a failed merge must not damage a previously valid output;
- an output path that aliases an input file must be rejected;
- use only the Python standard library unless evidence demonstrates that it is inadequate.

The goal does not prescribe a database, framework, streaming architecture, schema library, or canonicalization package.
