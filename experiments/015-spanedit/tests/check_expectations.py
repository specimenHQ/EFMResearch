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
            raise AssertionError("oracle received overlapping edits")
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


source = "0123456789"
edits = [(1, 3, "ABCD"), (3, 3, "!"), (5, 7, ""), (9, 9, "?")]
expected = stream_oracle(source, edits)
assert expected == "0ABCD!3478?9"
print(f"PASS — independent forward-streaming oracle derived {expected!r}")
