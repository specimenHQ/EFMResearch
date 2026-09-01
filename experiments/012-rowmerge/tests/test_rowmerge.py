import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rowmerge import DuplicateIdentifierError, MissingIdentifierColumn, parse_csv, reconcile_csv


class RowMergeTests(unittest.TestCase):
    def test_leading_zero_identifier_is_distinct(self):
        result = reconcile_csv("id,v\n001,L\n", "id,v\n1,R\n")
        self.assertEqual([r["id"] for r in result.left_only], ["001"])
        self.assertEqual([r["id"] for r in result.right_only], ["1"])
        self.assertEqual(result.matched, ())

    def test_large_digit_identifiers_remain_distinct(self):
        left = "id,v\n9007199254740992,a\n9007199254740993,b\n"
        right = "id,v\n9007199254740992,x\n9007199254740993,y\n"
        result = reconcile_csv(left, right)
        self.assertEqual([m.identifier for m in result.matched], ["9007199254740992", "9007199254740993"])

    def test_required_csv_quoting_cases(self):
        text = 'id,note\r\n001,"alpha,beta"\r\n002,"He said ""hi"""\r\n003,"line1\nline2"\r\n'
        fields, rows = parse_csv(text)
        self.assertEqual(fields, ["id", "note"])
        self.assertEqual(rows[0]["note"], "alpha,beta")
        self.assertEqual(rows[1]["note"], 'He said "hi"')
        self.assertEqual(rows[2]["note"], "line1\nline2")

    def test_duplicate_left_is_explicit_ambiguity(self):
        with self.assertRaises(DuplicateIdentifierError) as ctx:
            reconcile_csv("id,v\n001,a\n001,b\n", "id,v\n001,x\n")
        self.assertEqual(ctx.exception.groups[0].source, "left")
        self.assertEqual(ctx.exception.groups[0].identifier, "001")
        self.assertEqual(len(ctx.exception.groups[0].rows), 2)

    def test_duplicate_right_is_explicit_ambiguity(self):
        with self.assertRaises(DuplicateIdentifierError) as ctx:
            reconcile_csv("id,v\n001,a\n", "id,v\n001,x\n001,y\n")
        self.assertEqual(ctx.exception.groups[0].source, "right")

    def test_blank_ids_are_invalid_not_joined(self):
        result = reconcile_csv("id,v\n,one\nA,left\n", "id,v\n,two\nA,right\n")
        self.assertEqual(len(result.matched), 1)
        self.assertEqual(result.matched[0].identifier, "A")
        self.assertEqual([r["v"] for r in result.invalid_left], ["one"])
        self.assertEqual([r["v"] for r in result.invalid_right], ["two"])

    def test_result_order_is_independent_of_source_order(self):
        left_a = "id,v\nb,2\na,1\nd,4\n"
        left_b = "id,v\nd,4\na,1\nb,2\n"
        right_a = "id,v\nc,3\na,x\nb,y\n"
        right_b = "id,v\nb,y\nc,3\na,x\n"
        r1 = reconcile_csv(left_a, right_a)
        r2 = reconcile_csv(left_b, right_b)
        self.assertEqual([m.identifier for m in r1.matched], ["a", "b"])
        self.assertEqual([m.identifier for m in r2.matched], ["a", "b"])
        self.assertEqual([r["id"] for r in r1.left_only], ["d"])
        self.assertEqual([r["id"] for r in r2.left_only], ["d"])
        self.assertEqual([r["id"] for r in r1.right_only], ["c"])
        self.assertEqual([r["id"] for r in r2.right_only], ["c"])

    def test_matched_rows_preserve_parsed_fields(self):
        left = 'id,note\n001,"a,b"\n'
        right = 'id,note\n001,"line1\nline2"\n'
        result = reconcile_csv(left, right)
        self.assertEqual(result.matched[0].left["note"], "a,b")
        self.assertEqual(result.matched[0].right["note"], "line1\nline2")

    def test_unmatched_rows_on_both_sides(self):
        result = reconcile_csv("id,v\na,1\nb,2\n", "id,v\nb,x\nc,3\n")
        self.assertEqual([m.identifier for m in result.matched], ["b"])
        self.assertEqual([r["id"] for r in result.left_only], ["a"])
        self.assertEqual([r["id"] for r in result.right_only], ["c"])

    def test_missing_identifier_column_fails(self):
        with self.assertRaises(MissingIdentifierColumn):
            reconcile_csv("key,v\na,1\n", "id,v\na,2\n")

    def test_post_green_exact_unicode_identity(self):
        composed = "é"
        decomposed = "e\u0301"
        result = reconcile_csv(f"id,v\n{composed},left\nA,upper\n", f"id,v\n{decomposed},right\na,lower\n")
        self.assertEqual([r["id"] for r in result.left_only], ["A", composed])
        self.assertEqual([r["id"] for r in result.right_only], ["a", decomposed])
        self.assertEqual(result.matched, ())


if __name__ == "__main__":
    unittest.main(verbosity=2)
