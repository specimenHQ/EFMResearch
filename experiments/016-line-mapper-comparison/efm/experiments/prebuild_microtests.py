import random
import re

EXACT_SEPARATOR = re.compile(r"\r\n|\r|\n")


def scan_required(text):
    lines = []
    start = 0
    i = 0
    while i < len(text):
        if text[i] == "\r":
            end = i
            separator_end = i + 2 if i + 1 < len(text) and text[i + 1] == "\n" else i + 1
            lines.append((start, end, separator_end))
            start = separator_end
            i = separator_end
        elif text[i] == "\n":
            lines.append((start, i, i + 1))
            start = i + 1
            i += 1
        else:
            i += 1
    lines.append((start, len(text), len(text)))
    return tuple(lines)


def regex_oracle(text):
    lines = []
    start = 0
    for match in EXACT_SEPARATOR.finditer(text):
        lines.append((start, match.start(), match.end()))
        start = match.end()
    lines.append((start, len(text), len(text)))
    return tuple(lines)


def offset_to_position(spans, text_length, offset):
    if offset < 0 or offset > text_length:
        raise ValueError("invalid offset")
    for line, (start, end, _separator_end) in enumerate(spans):
        if start <= offset <= end:
            return line, offset - start
    raise ValueError("inside separator")


# A1: splitlines recognizes line boundaries outside the frozen separator set.
special = "a\u2028b\x85c\vD\fE"
parts = special.splitlines(keepends=True)
assert len(parts) == 5
assert regex_oracle(special) == ((0, len(special), len(special)),)
print("A1 FALSIFIED splitlines authority — non-required Unicode boundaries were split")

# A2: explicit scanner agrees with exact-separator regex oracle.
fixtures = [
    "",
    "abc",
    "a\n",
    "a\r",
    "a\r\n",
    "\n",
    "\r\n",
    "a\n\nb",
    "a\r\nb\rc\n",
    "a\u2028b\x85c",
]
for fixture in fixtures:
    assert scan_required(fixture) == regex_oracle(fixture)

rng = random.Random(16016)
alphabet = ["a", "b", "🙂", "\u0301", "\n", "\r", "\u2028", "\x85"]
for _ in range(500):
    fixture = "".join(rng.choice(alphabet) for _ in range(rng.randrange(0, 30)))
    assert scan_required(fixture) == regex_oracle(fixture)
print("A2 PASS — explicit scanner matched regex oracle on fixed + 500 seeded fixtures")

# A3: splitlines omits the required final empty logical line.
assert "".splitlines(keepends=True) == []
assert "a\n".splitlines(keepends=True) == ["a\n"]
assert "a\r".splitlines(keepends=True) == ["a\r"]
assert "a\r\n".splitlines(keepends=True) == ["a\r\n"]
assert regex_oracle("") == ((0, 0, 0),)
assert regex_oracle("a\r\n") == ((0, 1, 3), (3, 3, 3))
print("A3 CONFIRMED — empty/trailing final line requires explicit representation")

# A4: CRLF has valid outer boundaries and one invalid interior integer offset.
text = "a\r\nb"
spans = regex_oracle(text)
assert offset_to_position(spans, len(text), 1) == (0, 1)
try:
    offset_to_position(spans, len(text), 2)
    raise AssertionError("CRLF interior offset was accepted")
except ValueError:
    pass
assert offset_to_position(spans, len(text), 3) == (1, 0)
print("A4 PASS — CRLF outer boundaries valid; middle offset rejected")

# A5: code-point coordinates differ from encoded byte length.
unicode_text = "A🙂e\u0301B"
assert len(unicode_text) == 5
assert len(unicode_text.encode("utf-8")) == 9
assert unicode_text[1:2] == "🙂"
assert unicode_text[2:4] == "e\u0301"
print("A5 PASS — Python str coordinate scope is code-point based")

# A6: the independent regex oracle detects a plausible over-splitting design.
wrong = tuple(part for part in "a\u2028b".splitlines(keepends=True))
correct = regex_oracle("a\u2028b")
assert len(wrong) == 2 and correct == ((0, 3, 3),)
print("A6 PASS — exact-separator oracle detects convenience-API over-splitting")
