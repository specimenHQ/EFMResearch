from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rejected = load("mergesafe_v0_rejected", ROOT / "history" / "mergesafe_v0_rejected.py")
current = load("mergesafe_current", ROOT / "src" / "mergesafe.py")

# A8 falsifier: parsed-value equality is broader than v0's json.dumps rendering.
left = json.loads('{"id":"r1","n":1}')
right = json.loads('{"n":1.0,"id":"r1"}')
assert left == right
assert rejected.canonical_json(left) != rejected.canonical_json(right)

with tempfile.TemporaryDirectory() as td:
    d = Path(td)
    a = d / "a.jsonl"
    b = d / "b.jsonl"
    old_out = d / "old.jsonl"
    new_out = d / "new.jsonl"
    a.write_text('{"id":"r1","n":1}\n', encoding="utf-8")
    b.write_text('{"n":1.0,"id":"r1"}\n', encoding="utf-8")

    try:
        rejected.merge_files([a, b], old_out)
    except rejected.RecordConflictError:
        pass
    else:
        raise AssertionError("A8 falsifier failed: rejected v0 did not expose false conflict")

    assert current.merge_files([a, b], new_out) == 1
    assert new_out.read_text(encoding="utf-8") == '{"id":"r1","n":1}\n'

# A9 falsifier: duplicate object members were silently overwritten by v0.
duplicate = '{"id":"r1","x":1,"x":2}'
parsed_v0 = rejected.parse_record(duplicate, source=Path("probe.jsonl"), line_number=1)
assert parsed_v0["x"] == 2

try:
    current.parse_record(duplicate, source=Path("probe.jsonl"), line_number=1)
except current.InputRecordError as exc:
    assert "duplicate object key" in str(exc)
else:
    raise AssertionError("A9 correction failed: current parser accepted duplicate object members")

print("A8: FALSIFIED v0 — parsed-equal numeric spellings produced different canonical strings and false conflict.")
print("A8 correction: PASS — current project-canonical number rendering collapses 1 and 1.0 deterministically.")
print("A9: FALSIFIED v0 — duplicate object member names silently used last-write-wins parsing.")
print("A9 correction: PASS — current strict parser rejects duplicate object member names.")
