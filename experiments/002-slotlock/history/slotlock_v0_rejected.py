\
from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

class SlotLockError(ValueError):
    pass

def normalize_slot(value: str) -> str:
    try:
        dt = datetime.fromisoformat(value)
    except ValueError as exc:
        raise SlotLockError(f"invalid ISO-8601 timestamp: {value}") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise SlotLockError("timestamp must include a timezone offset")
    return dt.astimezone(timezone.utc).isoformat(timespec="microseconds")

class SlotStore:
    def __init__(self, db_path):
        self.con = sqlite3.connect(str(db_path), timeout=5)
        self.con.execute("""CREATE TABLE IF NOT EXISTS reservations(
            slot_utc TEXT PRIMARY KEY, slot_input TEXT NOT NULL,
            name TEXT NOT NULL, created_at_utc TEXT NOT NULL)""")
        self.con.execute("""CREATE TABLE IF NOT EXISTS events(
            id INTEGER PRIMARY KEY, event_type TEXT NOT NULL,
            slot_utc TEXT NOT NULL, name TEXT, at_utc TEXT NOT NULL)""")
        self.con.commit()

    def reserve(self, slot_input, name):
        slot_utc = normalize_slot(slot_input)
        now = datetime.now(timezone.utc).isoformat(timespec="microseconds")
        try:
            with self.con:
                self.con.execute("INSERT INTO reservations VALUES (?, ?, ?, ?)",
                                 (slot_utc, slot_input, name.strip(), now))
                self.con.execute(
                    "INSERT INTO events(event_type, slot_utc, name, at_utc) VALUES ('RESERVE', ?, ?, ?)",
                    (slot_utc, name.strip(), now))
            return True
        except sqlite3.IntegrityError:
            return False
