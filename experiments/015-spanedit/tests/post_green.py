import itertools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from spanedit import apply_edits


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


source = "α🙂bcde\u0301FGHIJ"
edits = [
    (0, 1, "Ω"),
    (1, 1, "<"),
    (1, 2, "EMOJI"),
    (2, 2, ">"),
    (4, 6, ""),
    (10, 10, "?"),
]

expected = stream_oracle(source, edits)
count = 0
for permutation in itertools.permutations(edits):
    assert apply_edits(source, permutation) == expected
    count += 1

print(f"PASS — {count} declaration permutations matched independent streaming oracle {expected!r}")
