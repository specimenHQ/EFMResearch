import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wallclock import Resolution, daily_occurrences, resolve_local

ZONE = "America/New_York"


def resolver_judge(fn):
    cases = [
        (
            datetime(2026, 1, 15, 9),
            "unique",
            ["2026-01-15T14:00:00+00:00"],
        ),
        (datetime(2026, 3, 8, 2, 30), "nonexistent", []),
        (
            datetime(2026, 11, 1, 1, 30),
            "ambiguous",
            ["2026-11-01T05:30:00+00:00", "2026-11-01T06:30:00+00:00"],
        ),
    ]

    for requested, expected_status, expected_utc in cases:
        result = fn(requested, ZONE)
        if result.status != expected_status:
            return False
        if [x.isoformat() for x in result.utc_instants] != expected_utc:
            return False
    return True


def schedule_judge(fn):
    results = fn(date(2026, 3, 7), date(2026, 3, 9), time(9), ZONE)
    return (
        [x.requested_local.hour for x in results] == [9, 9, 9]
        and [x.utc_instants[0].hour for x in results] == [14, 13, 13]
    )


def direct_fold_zero(requested, zone_name):
    zone = ZoneInfo(zone_name)
    instant = requested.replace(tzinfo=zone, fold=0)
    return Resolution(requested, zone_name, "unique", (instant,))


def offsets_differ_means_ambiguous(requested, zone_name):
    zone = ZoneInfo(zone_name)
    first = requested.replace(tzinfo=zone, fold=0)
    second = requested.replace(tzinfo=zone, fold=1)
    if first.utcoffset() != second.utcoffset():
        return Resolution(requested, zone_name, "ambiguous", (first, second))
    return Resolution(requested, zone_name, "unique", (first,))


def collapse_valid_folds(requested, zone_name):
    result = resolve_local(requested, zone_name)
    if result.status == "ambiguous":
        return Resolution(requested, zone_name, "unique", (result.instants[0],))
    return result


def shift_gap_forward(requested, zone_name):
    result = resolve_local(requested, zone_name)
    if result.status == "nonexistent":
        zone = ZoneInfo(zone_name)
        shifted = (requested + timedelta(hours=1)).replace(tzinfo=zone)
        return Resolution(requested, zone_name, "unique", (shifted,))
    return result


def fixed_utc_daily(start_date, end_date, local_time, zone_name):
    zone = ZoneInfo(zone_name)
    first = resolve_local(datetime.combine(start_date, local_time), zone_name)
    base_utc = first.utc_instants[0]
    results = []
    current = start_date
    index = 0

    while current <= end_date:
        instant = (base_utc + timedelta(days=index)).astimezone(zone)
        results.append(
            Resolution(datetime.combine(current, local_time), zone_name, "unique", (instant,))
        )
        current += timedelta(days=1)
        index += 1

    return results


def main():
    false_designs = [
        ("direct fold=0 attachment treated as unique", lambda: resolver_judge(direct_fold_zero)),
        ("offset difference alone treated as ambiguity", lambda: resolver_judge(offsets_differ_means_ambiguous)),
        ("valid repeated folds collapsed to one instant", lambda: resolver_judge(collapse_valid_folds)),
        ("nonexistent wall time silently shifted forward", lambda: resolver_judge(shift_gap_forward)),
        ("daily schedule advanced by fixed UTC 24-hour steps", lambda: schedule_judge(fixed_utc_daily)),
    ]

    rejected = 0
    for name, accepted_by_judge in false_designs:
        if accepted_by_judge():
            raise AssertionError(f"judge accepted known-false design: {name}")
        rejected += 1

    if not resolver_judge(resolve_local):
        raise AssertionError("judge rejected accepted resolver")
    if not schedule_judge(daily_occurrences):
        raise AssertionError("judge rejected accepted scheduler")

    print(f"PASS — judge rejected all {rejected} known-false designs")


if __name__ == "__main__":
    main()
