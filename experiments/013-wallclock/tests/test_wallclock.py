import sys
import unittest
from datetime import date, datetime, time, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wallclock import daily_occurrences, resolve_local


class WallClockTests(unittest.TestCase):
    ZONE = "America/New_York"

    def test_winter_unique(self):
        result = resolve_local(datetime(2026, 1, 15, 9), self.ZONE)
        self.assertEqual(result.status, "unique")
        self.assertEqual(
            [x.isoformat() for x in result.utc_instants],
            ["2026-01-15T14:00:00+00:00"],
        )

    def test_summer_unique(self):
        result = resolve_local(datetime(2026, 7, 15, 9), self.ZONE)
        self.assertEqual(result.status, "unique")
        self.assertEqual(
            [x.isoformat() for x in result.utc_instants],
            ["2026-07-15T13:00:00+00:00"],
        )

    def test_spring_gap_nonexistent(self):
        result = resolve_local(datetime(2026, 3, 8, 2, 30), self.ZONE)
        self.assertEqual(result.status, "nonexistent")
        self.assertEqual(result.instants, ())

    def test_fall_repeat_ambiguous(self):
        result = resolve_local(datetime(2026, 11, 1, 1, 30), self.ZONE)
        self.assertEqual(result.status, "ambiguous")
        self.assertEqual(
            [x.isoformat() for x in result.utc_instants],
            ["2026-11-01T05:30:00+00:00", "2026-11-01T06:30:00+00:00"],
        )

    def test_preserves_requested_local(self):
        requested = datetime(2026, 11, 1, 1, 30)
        result = resolve_local(requested, self.ZONE)
        self.assertEqual(result.requested_local, requested)
        self.assertTrue(all(x.replace(tzinfo=None) == requested for x in result.instants))

    def test_rejects_aware_request(self):
        with self.assertRaises(ValueError):
            resolve_local(datetime(2026, 1, 1, 9, tzinfo=timezone.utc), self.ZONE)

    def test_daily_range_is_inclusive(self):
        results = daily_occurrences(
            date(2026, 3, 7), date(2026, 3, 9), time(9), self.ZONE
        )
        self.assertEqual(
            [x.requested_local.date() for x in results],
            [date(2026, 3, 7), date(2026, 3, 8), date(2026, 3, 9)],
        )

    def test_daily_local_time_survives_spring_transition(self):
        results = daily_occurrences(
            date(2026, 3, 7), date(2026, 3, 9), time(9), self.ZONE
        )
        self.assertTrue(all(x.status == "unique" for x in results))
        self.assertEqual([x.instants[0].hour for x in results], [9, 9, 9])
        self.assertEqual([x.utc_instants[0].hour for x in results], [14, 13, 13])

    def test_daily_local_time_survives_fall_transition(self):
        results = daily_occurrences(
            date(2026, 10, 31), date(2026, 11, 2), time(9), self.ZONE
        )
        self.assertTrue(all(x.status == "unique" for x in results))
        self.assertEqual([x.instants[0].hour for x in results], [9, 9, 9])
        self.assertEqual([x.utc_instants[0].hour for x in results], [13, 14, 14])

    def test_daily_gap_is_reported_not_shifted(self):
        results = daily_occurrences(
            date(2026, 3, 7), date(2026, 3, 9), time(2, 30), self.ZONE
        )
        self.assertEqual(
            [x.status for x in results], ["unique", "nonexistent", "unique"]
        )

    def test_rejects_reversed_range(self):
        with self.assertRaises(ValueError):
            daily_occurrences(
                date(2026, 3, 9), date(2026, 3, 7), time(9), self.ZONE
            )

    def test_post_green_repeated_time_in_range(self):
        results = daily_occurrences(
            date(2026, 10, 31), date(2026, 11, 2), time(1, 30), self.ZONE
        )
        self.assertEqual(
            [x.status for x in results], ["unique", "ambiguous", "unique"]
        )
        self.assertEqual(sum(len(x.instants) for x in results), 4)
        self.assertTrue(
            all(x.requested_local.time() == time(1, 30) for x in results)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
