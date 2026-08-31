from datetime import datetime, timezone


def _instant(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        raise ValueError(f"timestamp lacks timezone: {value!r}")
    return dt.astimezone(timezone.utc)


def sort_timestamps(values):
    return sorted(values, key=_instant)
