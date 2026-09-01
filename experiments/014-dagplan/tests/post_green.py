import itertools
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dagplan import plan_stages

fixture = [
    ("F", ["D", "E"]),
    ("E", ["B", "C"]),
    ("D", ["A", "C"]),
    ("C", []),
    ("B", ["A"]),
    ("A", []),
]

dependencies = {task: tuple(deps) for task, deps in fixture}


@lru_cache(None)
def depth(task):
    return 0 if not dependencies[task] else 1 + max(depth(dep) for dep in dependencies[task])


by_depth = {}
for task in dependencies:
    by_depth.setdefault(depth(task), []).append(task)
expected = tuple(tuple(sorted(by_depth[level])) for level in sorted(by_depth))
assert expected == (("A", "C"), ("B", "D"), ("E",), ("F",))

count = 0
for permutation in itertools.permutations(fixture):
    assert plan_stages(permutation) == expected
    count += 1

print(f"PASS — {count} declaration permutations matched independent depth oracle {expected}")
