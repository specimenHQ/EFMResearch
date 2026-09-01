# Preimplementation Results — Experiment 013 WallClock

Protocol: v0.3
Runtime zone fixture: `America/New_York`

## A1 — direct timezone attachment is not validity classification

PASS / design constraint confirmed.

Fixture: requested local `2026-03-08 02:30:00`, during the spring-forward gap.

Directly attaching the zone produced two apparent aware values:

- fold 0: offset `-05:00`, maps to `07:30 UTC`, round-trips to `03:30 -04:00`;
- fold 1: offset `-04:00`, maps to `06:30 UTC`, round-trips to `01:30 -05:00`.

Neither candidate round-trips to the requested `02:30`. Direct attachment is therefore rejected as the validity authority.

## A2 — folds represent the repeated fall-back time

PASS.

Fixture: requested local `2026-11-01 01:30:00`.

- fold 0 → `05:30 UTC` (`-04:00`);
- fold 1 → `06:30 UTC` (`-05:00`).

Both round-trip to the requested wall time and resolve to different real instants.

## A3 — round-trip classification separates all three classes

PASS on controlled fixtures.

- ordinary winter `2026-01-15 09:00` → unique;
- ordinary summer `2026-07-15 09:00` → unique;
- spring gap `2026-03-08 02:30` → nonexistent;
- fall repeat `2026-11-01 01:30` → ambiguous with two UTC instants.

The classifier accepts only fold candidates whose UTC round-trip returns the exact requested naive local date/time, then deduplicates by UTC instant.

## A4 — fixed 24-hour UTC stepping does not preserve daily local wall time

PASS / naive strategy falsified.

- `2026-03-07 09:00 -05:00` + 24 UTC hours → `2026-03-08 10:00 -04:00`;
- `2026-10-31 09:00 -04:00` + 24 UTC hours → `2026-11-01 08:00 -05:00`.

Daily local scheduling must therefore iterate local calendar dates and resolve each wall time independently.

## A5 — ambiguity requires two valid distinct instants

PASS on controlled fixtures.

For ordinary winter and summer times, both fold settings can be constructed but resolve to the same UTC instant, so deduplication yields one unique occurrence. For the fall repeat, both folds round-trip and yield different UTC instants. For the spring gap, neither fold round-trips.

## A6 — runtime timezone availability

PASS.

`ZoneInfo('America/New_York')` loaded successfully in the experiment runtime.

## Evidence level

A1–A6: E2 controlled microtest evidence within the declared fixtures and one IANA timezone. No operational E6 or general claim about all timezone databases is made.
