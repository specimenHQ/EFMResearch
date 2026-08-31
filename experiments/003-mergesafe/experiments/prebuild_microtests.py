from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

results: list[tuple[str, bool, str]] = []

# A1 — parsed equivalence versus raw text.
raw_a = '{"id":"r1","name":"Ada","n":1}'
raw_b = '{ "n": 1, "name": "Ada", "id": "r1" }'
parsed_a = json.loads(raw_a)
parsed_b = json.loads(raw_b)
results.append((
    "A1",
    raw_a != raw_b and parsed_a == parsed_b,
    "Unequal JSON text parsed to equal objects, so raw text would create a false conflict.",
))

# A2 — chosen stdlib canonical representation.
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

results.append((
    "A2",
    canonical(parsed_a) == canonical(parsed_b),
    f"Equivalent objects canonicalized identically as {canonical(parsed_a)!r}.",
))

# A3 — staged commit: failure before replace must preserve old output.
with tempfile.TemporaryDirectory() as td:
    root = Path(td)
    output = root / "merged.jsonl"
    output.write_text('OLD\n', encoding="utf-8")
    temp_path = None
    try:
        fd, temp_name = tempfile.mkstemp(prefix=".merged.", suffix=".tmp", dir=root)
        temp_path = Path(temp_name)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write('NEW\n')
            f.flush()
            os.fsync(f.fileno())
        raise RuntimeError("injected failure before os.replace")
    except RuntimeError:
        if temp_path is not None and temp_path.exists():
            temp_path.unlink()
    results.append((
        "A3",
        output.read_text(encoding="utf-8") == 'OLD\n',
        "Injected pre-replace failure left the previous output bytes unchanged.",
    ))

# A4 — samefile catches symlink alias of an existing input.
with tempfile.TemporaryDirectory() as td:
    root = Path(td)
    source = root / "source.jsonl"
    alias = root / "alias.jsonl"
    source.write_text('{"id":"x"}\n', encoding="utf-8")
    alias.symlink_to(source)
    same = os.path.samefile(source, alias)
    results.append((
        "A4",
        same,
        "os.path.samefile identified a symlink alias as the same existing file.",
    ))

# A5 — deterministic bytes independent of input file/order, using id order + canonical JSON.
records_1 = [
    {"id": "b", "z": 2, "a": 1},
    {"id": "a", "name": "Ada"},
]
records_2 = [
    {"name": "Ada", "id": "a"},
    {"a": 1, "z": 2, "id": "b"},
]

def render(records):
    return "".join(canonical(r) + "\n" for r in sorted(records, key=lambda r: r["id"]))

out1 = render(records_1)
out2 = render(records_2)
results.append((
    "A5",
    out1 == out2,
    f"Reordered inputs and object keys produced byte-identical output ({len(out1)} bytes).",
))

# A6 — all needed mechanisms are present in stdlib.
required = all([
    callable(json.loads),
    callable(json.dumps),
    callable(tempfile.mkstemp),
    callable(os.replace),
    callable(os.path.samefile),
])
results.append((
    "A6",
    required,
    "json, tempfile, os.replace, fsync, and samefile are available in the Python standard library.",
))

for aid, ok, detail in results:
    print(f"{aid}: {'PASS' if ok else 'FAIL'} — {detail}")

if not all(ok for _, ok, _ in results):
    raise SystemExit(1)
