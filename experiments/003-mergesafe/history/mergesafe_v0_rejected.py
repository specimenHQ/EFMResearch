#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Iterable


class MergeSafeError(Exception):
    pass


class InputRecordError(MergeSafeError):
    pass


class RecordConflictError(MergeSafeError):
    pass


class PathAliasError(MergeSafeError):
    pass


def _reject_constant(token: str):
    raise ValueError(f"non-standard JSON constant: {token}")


def parse_record(text: str, *, source: Path, line_number: int) -> dict:
    try:
        value = json.loads(text, parse_constant=_reject_constant)
    except (json.JSONDecodeError, ValueError) as exc:
        raise InputRecordError(f"{source}:{line_number}: invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise InputRecordError(f"{source}:{line_number}: record must be a JSON object")
    record_id = value.get("id")
    if not isinstance(record_id, str) or not record_id:
        raise InputRecordError(f"{source}:{line_number}: record requires a nonempty string id")
    return value


def canonical_json(record: dict) -> str:
    return json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def _reject_output_alias(inputs: Iterable[Path], output: Path) -> None:
    if not output.exists():
        return
    for source in inputs:
        try:
            if os.path.samefile(source, output):
                raise PathAliasError(f"output aliases input file: {source}")
        except FileNotFoundError:
            # Missing inputs are reported naturally when opened.
            continue


def collect_records(inputs: list[Path]) -> dict[str, str]:
    accepted: dict[str, str] = {}
    origins: dict[str, tuple[Path, int]] = {}
    for source in inputs:
        with source.open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                text = raw.strip()
                if not text:
                    continue
                record = parse_record(text, source=source, line_number=line_number)
                record_id = record["id"]
                canonical = canonical_json(record)
                previous = accepted.get(record_id)
                if previous is None:
                    accepted[record_id] = canonical
                    origins[record_id] = (source, line_number)
                elif previous != canonical:
                    first_source, first_line = origins[record_id]
                    raise RecordConflictError(
                        f"conflicting id {record_id!r}: "
                        f"{first_source}:{first_line} vs {source}:{line_number}"
                    )
    return accepted


def render_records(records: dict[str, str]) -> str:
    return "".join(records[record_id] + "\n" for record_id in sorted(records))


def commit_output(output: Path, content: str) -> None:
    parent = output.parent
    fd, temp_name = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, output)
    except BaseException:
        try:
            temp_path.unlink(missing_ok=True)
        finally:
            raise


def merge_files(inputs: list[Path], output: Path) -> int:
    _reject_output_alias(inputs, output)
    records = collect_records(inputs)
    content = render_records(records)
    commit_output(output, content)
    return len(records)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Safely merge JSONL records by id")
    parser.add_argument("-o", "--output", required=True, type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        count = merge_files(args.inputs, args.output)
    except (MergeSafeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"MERGED {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
