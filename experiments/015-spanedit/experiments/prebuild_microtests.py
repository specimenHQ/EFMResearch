from itertools import permutations


def left_to_right(source, edits):
    out = source
    for start, end, replacement in sorted(edits, key=lambda edit: (edit[0], edit[1])):
        out = out[:start] + replacement + out[end:]
    return out


def right_to_left(source, edits):
    out = source
    ordered = sorted(
        edits,
        key=lambda edit: (edit[0], edit[1] > edit[0]),
        reverse=True,
    )
    for start, end, replacement in ordered:
        out = out[:start] + replacement + out[end:]
    return out


def conflict_reasons(edits):
    reasons = []
    for i, first in enumerate(edits):
        s1, e1, _ = first
        for j in range(i + 1, len(edits)):
            s2, e2, _ = edits[j]
            first_insert = s1 == e1
            second_insert = s2 == e2
            if first_insert and second_insert:
                if s1 == s2:
                    reasons.append((i, j, "duplicate insertion"))
            elif not first_insert and not second_insert:
                if max(s1, s2) < min(e1, e2):
                    reasons.append((i, j, "overlap"))
            else:
                position = s1 if first_insert else s2
                start, end = (s2, e2) if first_insert else (s1, e1)
                if start < position < end:
                    reasons.append((i, j, "interior insertion"))
    return reasons


def stream_oracle(source, edits):
    nonempty = sorted(
        [edit for edit in edits if edit[0] != edit[1]], key=lambda edit: edit[0]
    )
    insertions = {edit[0]: edit[2] for edit in edits if edit[0] == edit[1]}
    by_start = {edit[0]: edit for edit in nonempty}
    events = sorted(set([edit[0] for edit in nonempty] + list(insertions)))
    out = []
    cursor = 0
    for position in events:
        if position < cursor:
            continue
        out.append(source[cursor:position])
        if position in insertions:
            out.append(insertions[position])
        if position in by_start:
            start, end, replacement = by_start[position]
            out.append(replacement)
            cursor = end
        else:
            cursor = position
    out.append(source[cursor:])
    return "".join(out)


# A1 + A2: an expanding earlier edit shifts a later original coordinate.
source = "abcdef"
edits = [(1, 2, "WXYZ"), (4, 5, "Q")]
assert left_to_right(source, edits) == "aWXYQcdef"
assert right_to_left(source, edits) == "aWXYZcdQf"
assert stream_oracle(source, edits) == "aWXYZcdQf"
print("A1 FALSIFIED left-to-right authority — later target shifted")
print("A2 PASS — right-to-left matched independent streaming reconstruction")

# A3: adjacent spans and boundary insertions are valid; interior insertion conflicts.
for valid in (
    [(1, 3, "X"), (3, 5, "Y")],
    [(1, 3, "X"), (1, 1, "I")],
    [(1, 3, "X"), (3, 3, "I")],
):
    assert conflict_reasons(valid) == []
assert conflict_reasons([(1, 3, "X"), (2, 2, "I")])
print("A3 PASS — half-open boundary rules separated boundary and interior insertion")

# A4: Python string indices count code points, not UTF-8 bytes.
unicode_source = "A🙂e\u0301B"
assert len(unicode_source) == 5
assert unicode_source[1:2] == "🙂"
assert unicode_source[2:4] == "e\u0301"
assert len(unicode_source.encode("utf-8")) == 9
print("A4 PASS — Python str coordinate scope differs from UTF-8 byte length")

# A5: two insertions at one position are declaration-order dependent.
def sequential_insert(source, batch):
    out = source
    for start, end, replacement in batch:
        out = out[:start] + replacement + out[end:]
    return out

same_position = [(1, 1, "X"), (1, 1, "Y")]
assert sequential_insert("abc", same_position) == "aYXbc"
assert sequential_insert("abc", list(reversed(same_position))) == "aXYbc"
assert conflict_reasons(same_position)
print("A5 CONFIRMED ambiguity — same-position insertion order changes output")

# A6: streaming oracle agrees with right-to-left for every declaration permutation.
complex_source = "0123456789"
complex_edits = [(1, 3, "ABCD"), (3, 3, "!"), (5, 7, ""), (9, 9, "?")]
expected = stream_oracle(complex_source, complex_edits)
assert expected == "0ABCD!3478?9"
results = {right_to_left(complex_source, p) for p in permutations(complex_edits)}
assert results == {expected}
print("A6 PASS — 24 permutations matched independent streaming oracle")
