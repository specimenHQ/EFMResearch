from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

UTC = timezone.utc


@dataclass(frozen=True)
class Resolution:
    requested_local: datetime
    zone_name: str
    status: str
    instants: tuple[datetime, ...]

    @property
    def utc_instants(self) -> tuple[datetime, ...]:
        return tuple(instant.astimezone(UTC) for instant in self.instants)


def resolve_local(requested_local: datetime, zone_name: str) -> Resolution:
    if requested_local.tzinfo is not None:
        raise ValueError("requested_local must be naive")

    zone = ZoneInfo(zone_name)
    by_utc: dict[datetime, datetime] = {}

    for fold in (0, 1):
        attached = requested_local.replace(tzinfo=zone, fold=fold)
        utc = attached.astimezone(UTC)
        round_tripped = utc.astimezone(zone)

        if round_tripped.replace(tzinfo=None) == requested_local:
            by_utc[utc] = round_tripped

    instants = tuple(by_utc[key] for key in sorted(by_utc))

    if not instants:
        status = "nonexistent"
    elif len(instants) == 1:
        status = "unique"
    else:
        status = "ambiguous"

    return Resolution(requested_local, zone_name, status, instants)


def daily_occurrences(
    start_date: date,
    end_date: date,
    local_time: time,
    zone_name: str,
) -> list[Resolution]:
    if start_date > end_date:
        raise ValueError("start_date must be <= end_date")
    if local_time.tzinfo is not None:
        raise ValueError("local_time must be naive")

    results: list[Resolution] = []
    current = start_date

    while current <= end_date:
        results.append(resolve_local(datetime.combine(current, local_time), zone_name))
        current += timedelta(days=1)

    return results
