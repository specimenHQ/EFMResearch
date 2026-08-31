from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SOURCE = (ROOT / "src" / "mergesafe.py").read_text(encoding="utf-8")
TEST_SOURCE = (ROOT / "tests" / "test_mergesafe.py").read_text(encoding="utf-8")


def mutate_once(source: str, old: str, new: str) -> str:
    count = source.count(old)
    if count != 1:
        raise AssertionError(f"mutation target count was {count}, expected 1: {old!r}")
    return source.replace(old, new, 1)


def run_suite(source: str):
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "src").mkdir()
        (root / "tests").mkdir()
        (root / "src" / "mergesafe.py").write_text(source, encoding="utf-8")
        (root / "tests" / "test_mergesafe.py").write_text(TEST_SOURCE, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
            cwd=root,
            capture_output=True,
            text=True,
        )
        return proc.returncode, proc.stdout + proc.stderr


baseline_rc, baseline_output = run_suite(BASE_SOURCE)
if baseline_rc != 0:
    print(baseline_output)
    raise SystemExit("baseline judge did not accept the known-good implementation")

mutants = []
mutants.append((
    "permissive non-standard constants",
    mutate_once(BASE_SOURCE, "            parse_constant=_reject_constant,\n", ""),
    "test_nonstandard_json_constants_are_rejected",
))
mutants.append((
    "duplicate object members silently overwritten",
    mutate_once(BASE_SOURCE, "            object_pairs_hook=_unique_object,\n", ""),
    "test_duplicate_object_members_are_rejected",
))
mutants.append((
    "numeric representation treated as identity",
    mutate_once(BASE_SOURCE, "    normalized = value.normalize()\n", "    return str(value)\n    normalized = value.normalize()\n"),
    "test_numeric_equivalent_duplicates_collapse",
))
mutants.append((
    "conflicting duplicate silently accepted",
    mutate_once(BASE_SOURCE, "                elif previous != canonical:\n", "                elif False and previous != canonical:\n"),
    "test_conflicting_duplicate_preserves_previous_output",
))
mutants.append((
    "output/input alias check disabled",
    mutate_once(BASE_SOURCE, "def _reject_output_alias(inputs: Iterable[Path], output: Path) -> None:\n", "def _reject_output_alias(inputs: Iterable[Path], output: Path) -> None:\n    return\n"),
    "test_symlink_output_alias_is_rejected_without_source_change",
))
mutants.append((
    "record output order depends on insertion order",
    mutate_once(BASE_SOURCE, "for record_id in sorted(records)", "for record_id in records"),
    "test_output_is_independent_of_input_order_and_key_order",
))
mutants.append((
    "staged replace bypassed",
    mutate_once(BASE_SOURCE, "        os.replace(temp_path, output)\n", "        output.write_text(content, encoding=\"utf-8\")\n"),
    "test_replace_failure_preserves_previous_output_and_cleans_temp",
))

failures = []
print("baseline known-good: PASS")
for name, source, expected_test in mutants:
    rc, output = run_suite(source)
    detected = rc != 0 and expected_test in output
    status = "REJECTED" if detected else "ACCEPTED (JUDGE FAILURE)"
    print(f"{name}: {status}")
    if not detected:
        failures.append(name)
        print(output)

print(f"known-false mutants rejected: {len(mutants) - len(failures)}/{len(mutants)}")
if failures:
    raise SystemExit(1)
