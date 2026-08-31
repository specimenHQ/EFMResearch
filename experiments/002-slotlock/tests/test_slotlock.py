\
import sqlite3
import sys
import tempfile
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from slotlock import SlotLockError, SlotStore, normalize_slot


class SlotLockTests(unittest.TestCase):
    def test_equivalent_offsets_have_same_identity(self):
        self.assertEqual(
            normalize_slot("2026-09-01T10:00:00-06:00"),
            normalize_slot("2026-09-01T16:00:00+00:00"),
        )

    def test_naive_time_is_rejected(self):
        with self.assertRaises(SlotLockError):
            normalize_slot("2026-09-01T10:00:00")

    def test_equivalent_offset_double_booking_conflicts(self):
        with tempfile.TemporaryDirectory() as td:
            s = SlotStore(Path(td) / "db.sqlite3")
            try:
                self.assertTrue(s.reserve("2026-09-01T10:00:00-06:00", "Ada"))
                self.assertFalse(s.reserve("2026-09-01T16:00:00+00:00", "Grace"))
                self.assertEqual(len(s.list()), 1)
            finally:
                s.close()

    def test_persists_across_reopen(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db.sqlite3"
            s = SlotStore(db)
            self.assertTrue(s.reserve("2026-09-01T10:00:00-06:00", "Ada"))
            s.close()
            s2 = SlotStore(db)
            try:
                self.assertEqual([r.name for r in s2.list()], ["Ada"])
            finally:
                s2.close()

    def test_cancel_by_equivalent_offset(self):
        with tempfile.TemporaryDirectory() as td:
            s = SlotStore(Path(td) / "db.sqlite3")
            try:
                self.assertTrue(s.reserve("2026-09-01T10:00:00-06:00", "Ada"))
                self.assertTrue(s.cancel("2026-09-01T16:00:00+00:00"))
                self.assertEqual(s.list(), [])
            finally:
                s.close()

    def test_original_input_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            s = SlotStore(Path(td) / "db.sqlite3")
            try:
                original = "2026-09-01T10:00:00-06:00"
                s.reserve(original, "Ada")
                self.assertEqual(s.list()[0].slot_input, original)
            finally:
                s.close()

    def test_internal_failure_is_not_misreported_as_conflict_and_rolls_back(self):
        with tempfile.TemporaryDirectory() as td:
            s = SlotStore(Path(td) / "db.sqlite3")
            try:
                s.con.execute("""
                    CREATE TRIGGER fail_event
                    BEFORE INSERT ON events
                    BEGIN
                        SELECT RAISE(ABORT, 'forced internal failure');
                    END;
                """)
                with self.assertRaises(sqlite3.IntegrityError):
                    s.reserve("2026-09-01T10:00:00-06:00", "Ada")
                self.assertEqual(
                    s.con.execute("SELECT COUNT(*) FROM reservations").fetchone()[0], 0
                )
            finally:
                s.close()

    def test_concurrent_reservations_exactly_one_winner(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "db.sqlite3"
            initializer = SlotStore(db)
            initializer.close()

            barrier = threading.Barrier(8)
            outcomes = []
            errors = []
            lock = threading.Lock()

            def worker(i):
                store = SlotStore(db)
                try:
                    barrier.wait()
                    won = store.reserve("2026-09-01T10:00:00-06:00", f"user-{i}")
                    with lock:
                        outcomes.append(won)
                except Exception as exc:
                    with lock:
                        errors.append(repr(exc))
                finally:
                    store.close()

            threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]
            for t in threads: t.start()
            for t in threads: t.join()

            self.assertEqual(errors, [])
            self.assertEqual(outcomes.count(True), 1)
            self.assertEqual(outcomes.count(False), 7)

            s = SlotStore(db)
            try:
                self.assertEqual(len(s.list()), 1)
                events = s.con.execute(
                    "SELECT COUNT(*) FROM events WHERE event_type='RESERVE'"
                ).fetchone()[0]
                self.assertEqual(events, 1)
            finally:
                s.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
