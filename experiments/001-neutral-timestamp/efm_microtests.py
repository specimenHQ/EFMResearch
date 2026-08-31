from datetime import datetime, timezone


def parse(s):
    return datetime.fromisoformat(s[:-1] + "+00:00" if s.endswith("Z") else s)


def run():
    evidence = []

    # MT1: lexical order can be chronologically wrong.
    a = "2024-01-01T00:30:00+01:00"  # 2023-12-31 23:30Z
    b = "2023-12-31T23:45:00Z"       # 2023-12-31 23:45Z
    lexical = sorted([a, b])
    chronological = sorted([a, b], key=lambda s: parse(s).astimezone(timezone.utc))
    assert lexical != chronological
    assert chronological == [a, b]
    evidence.append("MT1 PASS: lexical sorting falsified")

    # MT2: required syntax is accepted by this runtime.
    for s in [
        "2026-08-31T14:00:00Z",
        "2026-08-31T08:00:00-06:00",
        "2026-08-31T14:00:00.123456+00:00",
    ]:
        assert parse(s).tzinfo is not None
    evidence.append("MT2 PASS: required syntax parsed")

    # MT3: offset-equivalent instants normalize equally.
    x = parse("2026-08-31T14:00:00Z").astimezone(timezone.utc)
    y = parse("2026-08-31T08:00:00-06:00").astimezone(timezone.utc)
    assert x == y
    evidence.append("MT3 PASS: offset-equivalent instants compare equal")

    # MT4: timezone-less timestamp is detectable.
    assert parse("2026-08-31T14:00:00").tzinfo is None
    evidence.append("MT4 PASS: naive timestamp detectable")

    # MT5: stable sort preserves input order for equal keys.
    items = [(0, "first"), (0, "second"), (1, "third")]
    assert [v for _, v in sorted(items, key=lambda p: p[0])] == ["first", "second", "third"]
    evidence.append("MT5 PASS: sort stability observed")

    return evidence


if __name__ == "__main__":
    for line in run():
        print(line)
