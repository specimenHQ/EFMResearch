from datetime import datetime, timezone


def _parse(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        raise ValueError(f"timestamp lacks timezone: {value!r}")
    return dt.astimezone(timezone.utc)


def sort_timestamps(values):
    decorated = [(_parse(value), index, value) for index, value in enumerate(values)]
    decorated.sort(key=lambda item: (item[0], item[1]))
    return [value for _, _, value in decorated]
