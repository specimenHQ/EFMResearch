import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from spanedit import (
    AmbiguousInsertionError,
    InvalidSpanError,
    OverlapError,
    apply_edits,
)


class SpanEditTests(unittest.TestCase):
    def test_empty_batch(self):
        self.assertEqual(apply_edits("abc", []), "abc")

    def test_expanding_replacement_preserves_later_original_coordinate(self):
        self.assertEqual(
            apply_edits("abcdef", [(1, 2, "WXYZ"), (4, 5, "Q")]),
            "aWXYZcdQf",
        )

    def test_deletion(self):
        self.assertEqual(apply_edits("abcdef", [(2, 4, "")]), "abef")

    def test_insertion(self):
        self.assertEqual(apply_edits("abc", [(1, 1, "XY")]), "aXYbc")

    def test_adjacent_nonempty_spans_allowed(self):
        self.assertEqual(
            apply_edits("abcdef", [(1, 3, "X"), (3, 5, "Y")]),
            "aXYf",
        )

    def test_start_boundary_insertion_precedes_replacement(self):
        self.assertEqual(
            apply_edits("abcdef", [(1, 3, "X"), (1, 1, "I")]),
            "aIXdef",
        )

    def test_end_boundary_insertion_follows_replacement(self):
        self.assertEqual(
            apply_edits("abcdef", [(1, 3, "X"), (3, 3, "I")]),
            "aXIdef",
        )

    def test_insertion_between_adjacent_replacements(self):
        self.assertEqual(
            apply_edits("abcdef", [(1, 3, "X"), (3, 5, "Y"), (3, 3, "!")]),
            "aX!Yf",
        )

    def test_interior_insertion_rejected(self):
        with self.assertRaises(OverlapError):
            apply_edits("abcdef", [(1, 4, "X"), (2, 2, "!")])

    def test_overlapping_nonempty_spans_rejected(self):
        with self.assertRaises(OverlapError):
            apply_edits("abcdef", [(1, 4, "X"), (3, 5, "Y")])

    def test_same_position_insertions_rejected(self):
        with self.assertRaises(AmbiguousInsertionError):
            apply_edits("abc", [(1, 1, "X"), (1, 1, "Y")])

    def test_invalid_bounds_rejected(self):
        for edit in [(-1, 1, "X"), (2, 1, "X"), (0, 4, "X")]:
            with self.subTest(edit=edit):
                with self.assertRaises(InvalidSpanError):
                    apply_edits("abc", [edit])

    def test_unicode_codepoint_coordinates(self):
        source = "A🙂e\u0301B"
        self.assertEqual(
            apply_edits(source, [(1, 2, "X"), (2, 4, "é")]),
            "AXéB",
        )

    def test_declaration_order_invariance(self):
        source = "0123456789"
        edits = [(1, 3, "ABCD"), (3, 3, "!"), (5, 7, ""), (9, 9, "?")]
        expected = "0ABCD!3478?9"
        for permutation in itertools.permutations(edits):
            self.assertEqual(apply_edits(source, permutation), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
