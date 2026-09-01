import re
from common_evaluation import evaluate, oracle_spans


class GenericIndex:
    def __init__(self, text, spans):
        self.text = text
        self.lines = tuple(spans)

    def line_count(self):
        return len(self.lines)

    def line_content_span(self, line):
        if line < 0:
            raise ValueError
        try:
            start, end, _ = self.lines[line]
        except Exception:
            raise ValueError
        return start, end

    def position_to_offset(self, line, column):
        start, end = self.line_content_span(line)
        if column < 0 or column > end - start:
            raise ValueError
        return start + column

    def offset_to_position(self, offset):
        if offset < 0 or offset > len(self.text):
            raise ValueError
        for line, (start, end, _sep_end) in enumerate(self.lines):
            if start <= offset <= end:
                return line, offset - start
        raise ValueError


class UnicodeOversplit(GenericIndex):
    def __init__(self, text):
        pattern = re.compile(r"\r\n|\r|\n|\u2028|\x85")
        spans = []
        start = 0
        for match in pattern.finditer(text):
            spans.append((start, match.start(), match.end()))
            start = match.end()
        spans.append((start, len(text), len(text)))
        super().__init__(text, spans)


class LFOnly(GenericIndex):
    def __init__(self, text):
        spans = []
        start = 0
        for i, ch in enumerate(text):
            if ch == "\n":
                spans.append((start, i, i + 1))
                start = i + 1
        spans.append((start, len(text), len(text)))
        super().__init__(text, spans)


class CRLFAsTwo(GenericIndex):
    def __init__(self, text):
        spans = []
        start = 0
        for i, ch in enumerate(text):
            if ch in "\r\n":
                spans.append((start, i, i + 1))
                start = i + 1
        spans.append((start, len(text), len(text)))
        super().__init__(text, spans)


class NoTrailingEmpty(GenericIndex):
    def __init__(self, text):
        spans = list(oracle_spans(text))
        if text.endswith(("\n", "\r")) and spans and spans[-1][0] == len(text):
            spans.pop()
        if not spans:
            spans = [(0, 0, 0)]
        super().__init__(text, spans)


class AcceptCRLFInterior(GenericIndex):
    def __init__(self, text):
        super().__init__(text, oracle_spans(text))

    def offset_to_position(self, offset):
        try:
            return super().offset_to_position(offset)
        except ValueError:
            previous = None
            for line, (start, end, separator_end) in enumerate(self.lines):
                if end < offset < separator_end:
                    previous = (line, end - start)
                    break
            if previous is not None:
                return previous
            raise


mutants = {
    "Unicode over-splitting": UnicodeOversplit,
    "LF-only separator handling": LFOnly,
    "CRLF treated as two separators": CRLFAsTwo,
    "trailing empty line omitted": NoTrailingEmpty,
    "CRLF interior offset accepted": AcceptCRLFInterior,
}

for name, candidate in mutants.items():
    checks, failures = evaluate(candidate)
    assert failures, f"judge accepted known-false candidate: {name}"
    print(f"REJECTED {name}: {len(failures)} failures across {checks} checks")

print("PASS — common evaluator rejected all 5 known-false line mappers")
