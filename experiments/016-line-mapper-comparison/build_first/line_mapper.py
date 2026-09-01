from __future__ import annotations


class LineMapError(ValueError):
    pass


class InvalidPositionError(LineMapError):
    pass


class InvalidOffsetError(LineMapError):
    pass


class LineIndex:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        self.text = text
        self.lines = self._scan_lines(text)

    @staticmethod
    def _scan_lines(text: str):
        lines = []
        start = 0
        i = 0
        while i < len(text):
            ch = text[i]
            if ch == "\r":
                end = i
                if i + 1 < len(text) and text[i + 1] == "\n":
                    separator_end = i + 2
                else:
                    separator_end = i + 1
                lines.append((start, end, separator_end))
                start = separator_end
                i = separator_end
            elif ch == "\n":
                end = i
                separator_end = i + 1
                lines.append((start, end, separator_end))
                start = separator_end
                i = separator_end
            else:
                i += 1
        lines.append((start, len(text), len(text)))
        return tuple(lines)

    def line_count(self) -> int:
        return len(self.lines)

    def line_content_span(self, line: int) -> tuple[int, int]:
        try:
            start, end, _ = self.lines[line]
        except (IndexError, TypeError):
            raise InvalidPositionError(f"invalid line: {line!r}") from None
        if line < 0:
            raise InvalidPositionError(f"invalid line: {line!r}")
        return start, end

    def position_to_offset(self, line: int, column: int) -> int:
        if not isinstance(line, int) or isinstance(line, bool):
            raise InvalidPositionError(f"invalid line: {line!r}")
        if not isinstance(column, int) or isinstance(column, bool):
            raise InvalidPositionError(f"invalid column: {column!r}")
        start, end = self.line_content_span(line)
        length = end - start
        if column < 0 or column > length:
            raise InvalidPositionError(
                f"column {column} outside line {line} content length {length}"
            )
        return start + column

    def offset_to_position(self, offset: int) -> tuple[int, int]:
        if not isinstance(offset, int) or isinstance(offset, bool):
            raise InvalidOffsetError(f"invalid offset: {offset!r}")
        if offset < 0 or offset > len(self.text):
            raise InvalidOffsetError(f"invalid offset: {offset!r}")

        for line, (start, end, _separator_end) in enumerate(self.lines):
            if start <= offset <= end:
                return line, offset - start

        raise InvalidOffsetError(
            f"offset {offset} lies inside a newline separator"
        )
