\
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


class SlotLockError(ValueError):
    pass


def normalize_slot(value: str) -> str:
    """Create one fixed-width UTC identity for a timezone-aware ISO-8601 instant."""
    try:
        dt = datetime.fromisoformat(value)
    except ValueError as exc:
        raise SlotLockError(f"invalid ISO-8601 timestamp: {value}") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise SlotLockError("timestamp must include a timezone offset")
    return dt.astimezone(timezone.utc).isoformat(timespec="microseconds")


@dataclass(frozen=True)
class Reservation:
    slot_utc: str
    slot_input: str
    name: str
    created_at_utc: str


class SlotStore:
    def __init__(self, db_path: str | Path):
        self.con = sqlite3.connect(str(db_path), timeout=5)
        self.con.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        with self.con:
            self.con.executescript("""
                CREATE TABLE IF NOT EXISTS reservations (
                    slot_utc TEXT PRIMARY KEY,
                    slot_input TEXT NOT NULL,
                    name TEXT NOT NULL CHECK(length(trim(name)) > 0),
                    created_at_utc TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    slot_utc TEXT NOT NULL,
                    name TEXT,
                    at_utc TEXT NOT NULL
                );
            """)

    def close(self) -> None:
        self.con.close()

    def reserve(self, slot_input: str, name: str) -> bool:
        slot_utc = normalize_slot(slot_input)
        clean_name = name.strip()
        if not clean_name:
            raise SlotLockError("name must not be empty")
        now = datetime.now(timezone.utc).isoformat(timespec="microseconds")

        # EFM-earned distinction:
        # OR IGNORE handles only the expected duplicate-slot path here.
        # Any failure in the subsequent event write propagates as a real error,
        # and the transaction rolls the reservation back.
        with self.con:
            cur = self.con.execute(
                """INSERT OR IGNORE INTO reservations(slot_utc, slot_input, name, created_at_utc)
                   VALUES (?, ?, ?, ?)""",
                (slot_utc, slot_input, clean_name, now),
            )
            if cur.rowcount == 0:
                return False
            self.con.execute(
                """INSERT INTO events(event_type, slot_utc, name, at_utc)
                   VALUES ('RESERVE', ?, ?, ?)""",
                (slot_utc, clean_name, now),
            )
        return True

    def cancel(self, slot_input: str) -> bool:
        slot_utc = normalize_slot(slot_input)
        now = datetime.now(timezone.utc).isoformat(timespec="microseconds")
        with self.con:
            row = self.con.execute(
                "SELECT name FROM reservations WHERE slot_utc = ?", (slot_utc,)
            ).fetchone()
            if row is None:
                return False
            self.con.execute("DELETE FROM reservations WHERE slot_utc = ?", (slot_utc,))
            self.con.execute(
                """INSERT INTO events(event_type, slot_utc, name, at_utc)
                   VALUES ('CANCEL', ?, ?, ?)""",
                (slot_utc, row["name"], now),
            )
        return True

    def list(self) -> list[Reservation]:
        rows = self.con.execute(
            """SELECT slot_utc, slot_input, name, created_at_utc
               FROM reservations ORDER BY slot_utc"""
        ).fetchall()
        return [Reservation(**dict(row)) for row in rows]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Tiny durable local reservation CLI")
    p.add_argument("--db", default="slotlock.sqlite3", help="SQLite database path")
    sub = p.add_subparsers(dest="command", required=True)

    reserve = sub.add_parser("reserve")
    reserve.add_argument("slot", help="timezone-aware ISO-8601 timestamp")
    reserve.add_argument("name")

    cancel = sub.add_parser("cancel")
    cancel.add_argument("slot")

    sub.add_parser("list")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    store = SlotStore(args.db)
    try:
        if args.command == "reserve":
            if store.reserve(args.slot, args.name):
                print("RESERVED")
                return 0
            print("CONFLICT")
            return 2
        if args.command == "cancel":
            if store.cancel(args.slot):
                print("CANCELLED")
                return 0
            print("NOT_FOUND")
            return 3
        if args.command == "list":
            for r in store.list():
                print(f"{r.slot_utc}\t{r.name}\t{r.slot_input}")
            return 0
    except SlotLockError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 4
    finally:
        store.close()


if __name__ == "__main__":
    raise SystemExit(main())
