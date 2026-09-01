import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dagplan import (
    CycleError,
    DuplicateDependencyError,
    DuplicateTaskError,
    UnknownDependencyError,
    plan_stages,
)


class DAGPlanTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(plan_stages([]), ())

    def test_independent_tasks_sorted(self):
        self.assertEqual(
            plan_stages([("z", []), ("a", []), ("m", [])]),
            (("a", "m", "z"),),
        )

    def test_chain(self):
        self.assertEqual(
            plan_stages([("C", ["B"]), ("A", []), ("B", ["A"])]),
            (("A",), ("B",), ("C",)),
        )

    def test_diamond(self):
        self.assertEqual(
            plan_stages([
                ("D", ["B", "C"]),
                ("C", ["A"]),
                ("B", ["A"]),
                ("A", []),
            ]),
            (("A",), ("B", "C"), ("D",)),
        )

    def test_declaration_order_invariance(self):
        fixture = [("C", ["A", "B"]), ("A", []), ("D", ["C"]), ("B", [])]
        expected = (("A", "B"), ("C",), ("D",))
        for perm in itertools.permutations(fixture):
            self.assertEqual(plan_stages(perm), expected)

    def test_duplicate_task_rejected(self):
        with self.assertRaises(DuplicateTaskError):
            plan_stages([("A", []), ("A", [])])

    def test_unknown_dependency_rejected(self):
        with self.assertRaises(UnknownDependencyError):
            plan_stages([("B", ["A"])])

    def test_duplicate_dependency_rejected(self):
        with self.assertRaises(DuplicateDependencyError):
            plan_stages([("A", []), ("B", ["A", "A"])])

    def test_two_node_cycle_rejected(self):
        with self.assertRaises(CycleError):
            plan_stages([("A", ["B"]), ("B", ["A"])])

    def test_self_cycle_rejected(self):
        with self.assertRaises(CycleError):
            plan_stages([("A", ["A"])])

    def test_exact_string_identity_is_case_sensitive(self):
        self.assertEqual(
            plan_stages([("a", []), ("A", []), ("B", ["A"]), ("b", ["a"])]),
            (("A", "a"), ("B", "b")),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
