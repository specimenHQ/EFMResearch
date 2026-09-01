from __future__ import annotations

from dataclasses import dataclass
import csv
import io
from typing import Mapping, Sequence


class RowMergeError(Exception):
    """Base error for RowMerge."""


class MissingIdentifierColumn(RowMergeError):
    pass


@dataclass(frozen=True)
class DuplicateGroup:
    source: str
    identifier: str
    rows: tuple[dict[str, str | None], ...]


class DuplicateIdentifierError(RowMergeError):
    def __init__(self, groups: Sequence[DuplicateGroup]):
        self.groups = tuple(groups)
        summary = ", ".join(f"{g.source}:{g.identifier!r}({len(g.rows)})" for g in self.groups)
        super().__init__(f"duplicate identifier ambiguity: {summary}")


@dataclass(frozen=True)
class Match:
    identifier: str
    left: dict[str, str | None]
    right: dict[str, str | None]


@dataclass(frozen=True)
class ReconcileResult:
    matched: tuple[Match, ...]
    left_only: tuple[dict[str, str | None], ...]
    right_only: tuple[dict[str, str | None], ...]
    invalid_left: tuple[dict[str, str | None], ...]
    invalid_right: tuple[dict[str, str | None], ...]


def parse_csv(text: str) -> tuple[list[str], list[dict[str, str | None]]]:
    stream = io.StringIO(text, newline="")
    reader = csv.DictReader(stream)
    if reader.fieldnames is None:
        return [], []
    fieldnames = list(reader.fieldnames)
    rows = [dict(row) for row in reader]
    return fieldnames, rows


def _index_rows(
    rows: Sequence[Mapping[str, str | None]],
    *,
    source: str,
    id_field: str,
) -> tuple[dict[str, dict[str, str | None]], list[dict[str, str | None]], list[DuplicateGroup]]:
    buckets: dict[str, list[dict[str, str | None]]] = {}
    invalid: list[dict[str, str | None]] = []

    for row in rows:
        copied = dict(row)
        identifier = copied.get(id_field)
        if identifier is None or identifier == "":
            invalid.append(copied)
            continue
        buckets.setdefault(identifier, []).append(copied)

    duplicates = [
        DuplicateGroup(source, identifier, tuple(items))
        for identifier, items in sorted(buckets.items())
        if len(items) > 1
    ]
    index = {
        identifier: items[0]
        for identifier, items in buckets.items()
        if len(items) == 1
    }
    return index, invalid, duplicates


def reconcile_csv(left_csv: str, right_csv: str, *, id_field: str = "id") -> ReconcileResult:
    left_fields, left_rows = parse_csv(left_csv)
    right_fields, right_rows = parse_csv(right_csv)

    if id_field not in left_fields:
        raise MissingIdentifierColumn(f"left CSV is missing identifier column {id_field!r}")
    if id_field not in right_fields:
        raise MissingIdentifierColumn(f"right CSV is missing identifier column {id_field!r}")

    left_index, invalid_left, dup_left = _index_rows(left_rows, source="left", id_field=id_field)
    right_index, invalid_right, dup_right = _index_rows(right_rows, source="right", id_field=id_field)

    duplicates = tuple(dup_left + dup_right)
    if duplicates:
        raise DuplicateIdentifierError(duplicates)

    left_ids = set(left_index)
    right_ids = set(right_index)

    matched = tuple(
        Match(identifier, left_index[identifier], right_index[identifier])
        for identifier in sorted(left_ids & right_ids)
    )
    left_only = tuple(left_index[identifier] for identifier in sorted(left_ids - right_ids))
    right_only = tuple(right_index[identifier] for identifier in sorted(right_ids - left_ids))

    return ReconcileResult(
        matched=matched,
        left_only=left_only,
        right_only=right_only,
        invalid_left=tuple(invalid_left),
        invalid_right=tuple(invalid_right),
    )
