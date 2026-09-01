import random
import re

SEP = re.compile(r"\r\n|\r|\n")


def oracle_spans(text):
    spans = []
    start = 0
    for match in SEP.finditer(text):
        spans.append((start, match.start(), match.end()))
        start = match.end()
    spans.append((start, len(text), len(text)))
    return tuple(spans)


def oracle_offset_position(spans, text_length, offset):
    if offset < 0 or offset > text_length:
        raise ValueError("invalid offset")
    for line, (start, end, _separator_end) in enumerate(spans):
        if start <= offset <= end:
            return line, offset - start
    raise ValueError("separator interior")


def expect_raises(callable_):
    try:
        callable_()
    except Exception:
        return True
    return False


def evaluate(LineIndex):
    failures = []
    checks = 0

    fixed = [
        "",
        "abc",
        "\n",
        "\r",
        "\r\n",
        "a\n",
        "a\r",
        "a\r\n",
        "a\n\nb",
        "a\r\nb\rc\n",
        "A🙂e\u0301B",
        "a\u2028b",
        "a\x85b",
        "a\v b\f c",
        "\u2028\x85",
    ]

    rng = random.Random(160160)
    alphabet = ["a", "b", "Z", "🙂", "\u0301", "\n", "\r", "\u2028", "\x85", "\v", "\f"]
    random_cases = [
        "".join(rng.choice(alphabet) for _ in range(rng.randrange(0, 45)))
        for _ in range(250)
    ]

    for case_no, text in enumerate(fixed + random_cases):
        expected = oracle_spans(text)
        try:
            index = LineIndex(text)
        except Exception as exc:
            failures.append(f"case {case_no}: construction failed: {exc!r}")
            continue

        checks += 1
        if index.line_count() != len(expected):
            failures.append(
                f"case {case_no}: line_count {index.line_count()} != {len(expected)}"
            )

        for line, (start, end, _separator_end) in enumerate(expected):
            checks += 1
            try:
                got_span = tuple(index.line_content_span(line))
            except Exception as exc:
                failures.append(f"case {case_no} line {line}: span raised {exc!r}")
                continue
            if got_span != (start, end):
                failures.append(
                    f"case {case_no} line {line}: span {got_span} != {(start, end)}"
                )

            for column in range(end - start + 1):
                expected_offset = start + column
                checks += 2
                try:
                    got_offset = index.position_to_offset(line, column)
                except Exception as exc:
                    failures.append(
                        f"case {case_no} {(line,column)}: position_to_offset raised {exc!r}"
                    )
                    continue
                if got_offset != expected_offset:
                    failures.append(
                        f"case {case_no} {(line,column)}: offset {got_offset} != {expected_offset}"
                    )
                try:
                    got_position = tuple(index.offset_to_position(expected_offset))
                except Exception as exc:
                    failures.append(
                        f"case {case_no} offset {expected_offset}: offset_to_position raised {exc!r}"
                    )
                    continue
                if got_position != (line, column):
                    failures.append(
                        f"case {case_no} offset {expected_offset}: position {got_position} != {(line,column)}"
                    )

        for offset in range(len(text) + 1):
            try:
                expected_position = oracle_offset_position(expected, len(text), offset)
                valid = True
            except ValueError:
                valid = False
                expected_position = None
            checks += 1
            try:
                got = tuple(index.offset_to_position(offset))
                raised = False
            except Exception:
                raised = True
                got = None
            if valid:
                if raised or got != expected_position:
                    failures.append(
                        f"case {case_no} offset {offset}: got {got if not raised else 'RAISE'} != {expected_position}"
                    )
            elif not raised:
                failures.append(
                    f"case {case_no} offset {offset}: separator-interior offset accepted as {got}"
                )

        checks += 4
        if not expect_raises(lambda: index.line_content_span(-1)):
            failures.append(f"case {case_no}: negative line accepted")
        if not expect_raises(lambda: index.line_content_span(len(expected))):
            failures.append(f"case {case_no}: past-end line accepted")
        if not expect_raises(lambda: index.position_to_offset(0, -1)):
            failures.append(f"case {case_no}: negative column accepted")
        if not expect_raises(lambda: index.offset_to_position(len(text) + 1)):
            failures.append(f"case {case_no}: past-end offset accepted")

    return checks, failures
