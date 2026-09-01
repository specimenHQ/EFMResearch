from __future__ import annotations

from dataclasses import dataclass


class LineMapError(ValueError):
    pass


class InvalidPositionError(LineMapError):
    pass


class InvalidOffsetError(LineMapError):
    pass


@dataclass(frozen=True)
class LineSpan:
    start: int
    end: int
    separator_end: int


def _scan(text: str) -> tuple[LineSpan, ...]:
    spans = []
    start = 0
    i = 0

    while i < len(text):
        if text[i] == "\r":
            separator_end = i + 2 if i + 1 < len(text) and text[i + 1] == "\n" else i + 1
            spans.append(LineSpan(start, i, separator_end))
            start = separator_end
            i = separator_end
        elif text[i] == "\n":
            spans.append(LineSpan(start, i, i + 1))
            start = i + 1
            i += 1
        else:
            i += 1

    spans.append(LineSpan(start, len(text), len(text)))
    return tuple(spans)


class LineIndex:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        self.lines = _scan(text)

    def line_count(self) -> int:
        return len(self.lines)

    def line_content_span(self, line: int) -> tuple[int, int]:
        if not isinstance(line, int) or isinstance(line, bool) or line < 0:
            raise InvalidPositionError(f"invalid line: {line!r}")
        try:
            span = self.lines[line]
        except IndexError:
            raise InvalidPositionError(f"invalid line: {line!r}") from None
        return span.start, span.end

    def position_to_offset(self, line: int, column: int) -> int:
        if not isinstance(column, int) or isinstance(column, bool) or column < 0:
            raise InvalidPositionError(f"invalid column: {column!r}")
        start, end = self.line_content_span(line)
        if column > end - start:
            raise InvalidPositionError(
                f"column {column} outside line {line} content length {end - start}"
            )
        return start + column

    def offset_to_position(self, offset: int) -> tuple[int, int]:
        if (
            not isinstance(offset, int)
            or isinstance(offset, bool)
            or offset < 0
            or offset > len(self.text)
        ):
            raise InvalidOffsetError(f"invalid offset: {offset!r}")

        for line, span in enumerate(self.lines):
            if span.start <= offset <= span.end:
                return line, offset - span.start

        raise InvalidOffsetError(
            f"offset {offset} lies inside a newline separator"
        )
