import random
from common_evaluation import oracle_spans, oracle_offset_position


def evaluate(LineIndex):
    failures = []
    checks = 0
    rng = random.Random(160161)
    alphabet = [
        "a", "b", "Z", "0", "🙂", "界", "\u0301",
        "\n", "\r", "\u2028", "\x85", "\v", "\f"
    ]

    cases = [
        "".join(rng.choice(alphabet) for _ in range(rng.randrange(0, 101)))
        for _ in range(1000)
    ]
    cases += [
        "\r\n" * 40,
        "\n\r" * 40,
        "🙂\r\n界\rZ\n\u2028\x85",
        "\u2028" * 50 + "\r\n" + "\x85" * 50,
    ]

    for case_no, text in enumerate(cases):
        expected = oracle_spans(text)
        index = LineIndex(text)

        checks += 1
        if index.line_count() != len(expected):
            failures.append(f"case {case_no}: line count mismatch")

        for line, (start, end, _sep_end) in enumerate(expected):
            checks += 1
            if tuple(index.line_content_span(line)) != (start, end):
                failures.append(f"case {case_no} line {line}: span mismatch")
            for col in range(end - start + 1):
                checks += 2
                off = index.position_to_offset(line, col)
                if off != start + col:
                    failures.append(f"case {case_no} line {line} col {col}: offset mismatch")
                if tuple(index.offset_to_position(off)) != (line, col):
                    failures.append(f"case {case_no} offset {off}: roundtrip mismatch")

        for offset in range(len(text) + 1):
            checks += 1
            try:
                expected_pos = oracle_offset_position(expected, len(text), offset)
                should_raise = False
            except ValueError:
                expected_pos = None
                should_raise = True
            try:
                got = tuple(index.offset_to_position(offset))
                raised = False
            except Exception:
                got = None
                raised = True
            if should_raise != raised:
                failures.append(f"case {case_no} offset {offset}: validity mismatch")
            elif not should_raise and got != expected_pos:
                failures.append(f"case {case_no} offset {offset}: position mismatch")

    return checks, failures
