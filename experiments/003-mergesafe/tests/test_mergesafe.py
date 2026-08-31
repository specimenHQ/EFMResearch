from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import mergesafe


class MergeSafeIntegrationTests(unittest.TestCase):
    def write(self, path: Path, text: str) -> Path:
        path.write_text(text, encoding="utf-8")
        return path

    def test_equivalent_duplicates_collapse_and_output_is_canonical(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"r1","name":"Ada","n":1}\n')
            b = self.write(d / "b.jsonl", '{ "n": 1, "name": "Ada", "id": "r1" }\n')
            out = d / "out.jsonl"
            self.assertEqual(mergesafe.merge_files([a, b], out), 1)
            self.assertEqual(out.read_text(encoding="utf-8"), '{"id":"r1","n":1,"name":"Ada"}\n')

    def test_conflicting_duplicate_preserves_previous_output(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"r1","value":1}\n')
            b = self.write(d / "b.jsonl", '{"id":"r1","value":2}\n')
            out = self.write(d / "out.jsonl", 'PREVIOUS\n')
            with self.assertRaises(mergesafe.RecordConflictError):
                mergesafe.merge_files([a, b], out)
            self.assertEqual(out.read_text(encoding="utf-8"), 'PREVIOUS\n')

    def test_malformed_input_reports_context_and_preserves_output(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"ok"}\nnot-json\n')
            out = self.write(d / "out.jsonl", 'PREVIOUS\n')
            with self.assertRaisesRegex(mergesafe.InputRecordError, r'a\.jsonl:2:'):
                mergesafe.merge_files([a], out)
            self.assertEqual(out.read_text(encoding="utf-8"), 'PREVIOUS\n')

    def test_nonstandard_json_constants_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"r1","value":NaN}\n')
            out = d / "out.jsonl"
            with self.assertRaises(mergesafe.InputRecordError):
                mergesafe.merge_files([a], out)
            self.assertFalse(out.exists())

    def test_output_is_independent_of_input_order_and_key_order(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"z":2,"id":"b","a":1}\n')
            b = self.write(d / "b.jsonl", '{"name":"Ada","id":"a"}\n')
            out1 = d / "out1.jsonl"
            out2 = d / "out2.jsonl"
            mergesafe.merge_files([a, b], out1)
            mergesafe.merge_files([b, a], out2)
            self.assertEqual(out1.read_bytes(), out2.read_bytes())
            self.assertEqual(
                out1.read_text(encoding="utf-8"),
                '{"id":"a","name":"Ada"}\n{"a":1,"id":"b","z":2}\n',
            )

    def test_symlink_output_alias_is_rejected_without_source_change(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            source = self.write(d / "source.jsonl", '{"id":"r1"}\n')
            original = source.read_bytes()
            alias = d / "alias.jsonl"
            alias.symlink_to(source)
            with self.assertRaises(mergesafe.PathAliasError):
                mergesafe.merge_files([source], alias)
            self.assertEqual(source.read_bytes(), original)

    def test_replace_failure_preserves_previous_output_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            source = self.write(d / "source.jsonl", '{"id":"r1"}\n')
            out = self.write(d / "out.jsonl", 'PREVIOUS\n')
            with mock.patch.object(mergesafe.os, "replace", side_effect=OSError("injected replace failure")):
                with self.assertRaises(OSError):
                    mergesafe.merge_files([source], out)
            self.assertEqual(out.read_text(encoding="utf-8"), 'PREVIOUS\n')
            self.assertEqual(list(d.glob('.out.jsonl.*.tmp')), [])

    def test_blank_and_missing_id_are_rejected_before_output_change(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            source = self.write(d / "source.jsonl", '{}\n')
            out = self.write(d / "out.jsonl", 'PREVIOUS\n')
            with self.assertRaises(mergesafe.InputRecordError):
                mergesafe.merge_files([source], out)
            self.assertEqual(out.read_text(encoding="utf-8"), 'PREVIOUS\n')

    def test_numeric_equivalent_duplicates_collapse(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"r1","n":1}\n')
            b = self.write(d / "b.jsonl", '{"n":1.0,"id":"r1"}\n')
            out = d / "out.jsonl"
            self.assertEqual(mergesafe.merge_files([a, b], out), 1)
            self.assertEqual(out.read_text(encoding="utf-8"), '{"id":"r1","n":1}\n')

    def test_duplicate_object_members_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            source = self.write(d / "source.jsonl", '{"id":"r1","x":1,"x":2}\n')
            out = self.write(d / "out.jsonl", 'PREVIOUS\n')
            with self.assertRaisesRegex(mergesafe.InputRecordError, "duplicate object key"):
                mergesafe.merge_files([source], out)
            self.assertEqual(out.read_text(encoding="utf-8"), 'PREVIOUS\n')

    def test_boolean_and_number_are_not_equivalent(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            a = self.write(d / "a.jsonl", '{"id":"r1","v":true}\n')
            b = self.write(d / "b.jsonl", '{"id":"r1","v":1}\n')
            out = d / "out.jsonl"
            with self.assertRaises(mergesafe.RecordConflictError):
                mergesafe.merge_files([a, b], out)

    def test_large_valid_number_does_not_overflow_to_nonfinite(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            source = self.write(d / "source.jsonl", '{"id":"r1","n":1e400}\n')
            out = d / "out.jsonl"
            self.assertEqual(mergesafe.merge_files([source], out), 1)
            self.assertEqual(out.read_text(encoding="utf-8"), '{"id":"r1","n":1e400}\n')


if __name__ == "__main__":
    unittest.main(verbosity=2)
