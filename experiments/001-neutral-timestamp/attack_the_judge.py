import importlib.util
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("common", ROOT / "common_adversarial_tests.py")
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)

class LexicalSorter:
    @staticmethod
    def sort_timestamps(values):
        return sorted(values)

class AcceptsNaive:
    @staticmethod
    def sort_timestamps(values):
        def key(s):
            return datetime.fromisoformat(s[:-1] + "+00:00" if s.endswith("Z") else s)
        return sorted(values, key=key)

class UnstableEqualInstant:
    @staticmethod
    def sort_timestamps(values):
        def key(s):
            dt = datetime.fromisoformat(s[:-1] + "+00:00" if s.endswith("Z") else s)
            if dt.tzinfo is None:
                raise ValueError("naive")
            return (dt.timestamp(), s)  # text tie-breaker intentionally destroys caller order
        return sorted(values, key=key)

for name, candidate in [
    ("known-bad lexical sorter", LexicalSorter),
    ("known-bad naive-accepting sorter", AcceptsNaive),
    ("known-bad unstable-equal sorter", UnstableEqualInstant),
]:
    result = common.run_arm(name, candidate)
    print(f"{name}: {len(result['failures'])} failures detected")
    for failure in result['failures']:
        print(f"  DETECTED: {failure}")
    if not result['failures']:
        raise SystemExit(f"judge failed to reject {name}")
