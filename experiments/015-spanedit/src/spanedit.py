from __future__ import annotations


class EditError(ValueError):
    pass


class InvalidSpanError(EditError):
    pass


class OverlapError(EditError):
    pass


class AmbiguousInsertionError(EditError):
    pass


def _validate_edits(source: str, edits):
    if not isinstance(source, str):
        raise TypeError("source must be a string")

    validated = []
    for edit in edits:
        try:
            start, end, replacement = edit
        except Exception as exc:
            raise TypeError("each edit must be (start, end, replacement)") from exc

        if (
            not isinstance(start, int)
            or isinstance(start, bool)
            or not isinstance(end, int)
            or isinstance(end, bool)
        ):
            raise TypeError("edit indices must be integers")
        if not isinstance(replacement, str):
            raise TypeError("replacement must be a string")
        if start < 0 or end < 0 or start > end or end > len(source):
            raise InvalidSpanError(
                f"invalid span [{start},{end}) for source length {len(source)}"
            )
        validated.append((start, end, replacement))

    for i, first in enumerate(validated):
        s1, e1, _ = first
        first_insert = s1 == e1
        for second in validated[i + 1 :]:
            s2, e2, _ = second
            second_insert = s2 == e2

            if first_insert and second_insert:
                if s1 == s2:
                    raise AmbiguousInsertionError(
                        f"multiple insertions at original position {s1}"
                    )
                continue

            if not first_insert and not second_insert:
                if max(s1, s2) < min(e1, e2):
                    raise OverlapError(
                        f"overlapping spans [{s1},{e1}) and [{s2},{e2})"
                    )
                continue

            position = s1 if first_insert else s2
            start, end = (s2, e2) if first_insert else (s1, e1)
            if start < position < end:
                raise OverlapError(
                    f"insertion at {position} lies inside edited span [{start},{end})"
                )

    return validated


def apply_edits(source: str, edits):
    """Apply original-coordinate edits deterministically and return the new string."""
    validated = _validate_edits(source, edits)

    # Greater original positions are changed first. At an equal start coordinate,
    # a nonempty edit is applied before a boundary insertion so the insertion
    # appears before the replacement in the final text.
    ordered = sorted(
        validated,
        key=lambda edit: (edit[0], edit[1] > edit[0]),
        reverse=True,
    )

    out = source
    for start, end, replacement in ordered:
        out = out[:start] + replacement + out[end:]
    return out
