import importlib.util
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent
SEED = 8675309
RANDOM_CASES = 500


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fmt(utc_dt, offset_minutes, use_z, fractional):
    local = utc_dt + timedelta(minutes=offset_minutes)
    base = local.strftime("%Y-%m-%dT%H:%M:%S")
    if fractional:
        base += f".{local.microsecond:06d}"
    if offset_minutes == 0 and use_z:
        return base + "Z"
    sign = "+" if offset_minutes >= 0 else "-"
    m = abs(offset_minutes)
    return f"{base}{sign}{m // 60:02d}:{m % 60:02d}"


def generated_fixture():
    rng = random.Random(SEED)
    base = datetime(2025, 1, 1, tzinfo=timezone.utc)
    entries = []
    previous_instant = None

    offsets = list(range(-12 * 60, 14 * 60 + 1, 15))
    for i in range(RANDOM_CASES):
        # About 1 in 8 entries intentionally duplicates the previous instant
        # but is rendered with a potentially different offset/representation.
        if previous_instant is not None and rng.randrange(8) == 0:
            instant = previous_instant
        else:
            seconds = rng.randint(-20_000_000, 20_000_000)
            micros = rng.choice([0, 0, 0, 123456, 500000, 999999])
            instant = base + timedelta(seconds=seconds, microseconds=micros)
        previous_instant = instant

        offset = rng.choice(offsets)
        use_z = rng.choice([True, False])
        fractional = instant.microsecond != 0
        text = fmt(instant, offset, use_z, fractional)
        entries.append((instant, i, text))

    shuffled = entries[:]
    rng.shuffle(shuffled)
    values = [text for _, _, text in shuffled]

    # Stability must refer to order in the actual caller input, not generation order.
    expected = [
        text
        for _, _, text in sorted(
            [(instant, input_index, text) for input_index, (instant, _, text) in enumerate(shuffled)],
            key=lambda row: (row[0], row[1]),
        )
    ]
    return values, expected


def run_arm(label, mod):
    failures = []
    checks = 0

    def check(condition, name):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(name)

    # Targeted offset/date-boundary case where lexical order is wrong.
    targeted = [
        "2023-12-31T23:45:00Z",
        "2024-01-01T00:30:00+01:00",
        "2023-12-31T18:50:00-05:00",
    ]
    targeted_expected = [
        "2024-01-01T00:30:00+01:00",  # 23:30Z
        "2023-12-31T23:45:00Z",       # 23:45Z
        "2023-12-31T18:50:00-05:00", # 23:50Z
    ]
    check(mod.sort_timestamps(targeted) == targeted_expected, "targeted offset/date-boundary ordering")

    # Equal instant, different textual representations; original order must survive.
    equal = [
        "2026-08-31T08:00:00-06:00",
        "2026-08-31T14:00:00Z",
        "2026-08-31T15:00:00+01:00",
    ]
    check(mod.sort_timestamps(equal) == equal, "stable equal-instant ordering")

    # Fractional seconds.
    fractional = [
        "2026-08-31T14:00:00.900000Z",
        "2026-08-31T14:00:00.100000Z",
        "2026-08-31T14:00:00.500000Z",
    ]
    check(mod.sort_timestamps(fractional) == [fractional[1], fractional[2], fractional[0]], "fractional seconds")

    # Caller input must not be mutated.
    original = targeted[:]
    mod.sort_timestamps(original)
    check(original == targeted, "input non-mutation")

    # Sequence need not be a list.
    check(mod.sort_timestamps(tuple(targeted)) == targeted_expected, "tuple input")

    # Naive timestamp must be rejected explicitly as ValueError.
    checks += 1
    try:
        mod.sort_timestamps(["2026-08-31T14:00:00"])
        failures.append("naive timestamp rejection")
    except ValueError:
        pass
    except Exception as exc:
        failures.append(f"naive timestamp wrong exception: {type(exc).__name__}")

    # Fresh randomized fixture generated only after both implementations were frozen.
    values, expected = generated_fixture()
    check(mod.sort_timestamps(values) == expected, f"{RANDOM_CASES}-entry randomized ordering/stability fixture")

    return {"arm": label, "checks": checks, "failures": failures}


def main():
    arms = [
        ("build-first", load("build_first", "build_first.py")),
        ("EFM", load("efm", "efm.py")),
    ]
    results = [run_arm(label, mod) for label, mod in arms]
    for result in results:
        print(f"{result['arm']}: {result['checks']} checks, {len(result['failures'])} failures")
        for failure in result["failures"]:
            print(f"  FAIL: {failure}")
    raise SystemExit(1 if any(r["failures"] for r in results) else 0)


if __name__ == "__main__":
    main()
