# Preregistration — Experiment 016 Controlled Comparison

Date: 2026-08-31  
Track: build-first vs EFM controlled comparison  
Active boundary: non-cyber

## Candidate tasks fixed before selection

1. `rename_planner` — plan collision-safe local batch file renames including cycles.
2. `bucketizer` — aggregate integer observations into deterministic half-open numeric buckets including negative values and boundaries.
3. `decimal_prorater` — prorate an exact decimal amount across weighted periods while conserving the final smallest-unit total.
4. `workflow_fold` — fold ordered workflow events through a declared finite-state transition table and identify the first invalid transition.
5. `line_mapper` — map logical line/column positions to Python Unicode string offsets and back across mixed newline conventions.

Selection method: Python `secrets.choice` over the five fixed candidate identifiers.

**Selected task:** `line_mapper`

## Frozen task requirements

Implement a small Python standard-library-only line index for one in-memory Unicode string.

Logical line separators:
- `\n`;
- `\r\n` treated as one logical separator;
- lone `\r` treated as one logical separator.

Required behavior:
- zero-based line numbers and zero-based columns;
- coordinates count Python Unicode code points, not UTF-8 bytes or grapheme clusters;
- every logical line has a content span excluding its separator;
- empty text contains one empty logical line;
- a trailing line separator creates a final empty logical line;
- `position_to_offset(line, column)` accepts columns from 0 through the line-content length inclusive and maps them to original-string offsets;
- `offset_to_position(offset)` accepts offsets from 0 through `len(text)` inclusive only when that offset is a line-content position; offsets pointing inside newline separator code points are rejected;
- the end offset of a line's content maps to `(line, content_length)`;
- the final `len(text)` offset maps to the final logical line's end position;
- invalid line, column, offset, and newline-interior offsets are rejected;
- round-trip must hold for every valid logical content position: `offset_to_position(position_to_offset(line,column)) == (line,column)`.

No file I/O, editor integration, byte-offset API, grapheme segmentation, or cybersecurity claim.

## Experimental order

1. Write the build-first implementation directly from the requirements with no exploratory tests or microtests.
2. Freeze its source and SHA-256 before EFM investigation begins.
3. Run the EFM arm under unchanged Protocol v0.3: goal/decision/assumption records, prebuild completeness, microtests, then implementation.
4. Freeze the EFM implementation and SHA-256.
5. Only after both implementations are frozen, create one common adversarial evaluation and an independent reference oracle.
6. Attack the common evaluator with known-false implementations before interpreting candidate results.
7. Record correctness, rework, implementation size, process/test overhead, architecture decisions, and whether EFM changed the delivered outcome.
8. Preserve a null result if build-first performs equally well.

No exact common evaluation fixtures are authored before both implementations are frozen.