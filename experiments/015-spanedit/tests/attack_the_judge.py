import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from spanedit import apply_edits


def verify(candidate):
    try:
        if candidate("abcdef", [(1, 2, "WXYZ"), (4, 5, "Q")]) != "aWXYZcdQf":
            return False
        if candidate("abcdef", [(1, 3, "X"), (3, 3, "!")]) != "aX!def":
            return False
    except Exception:
        return False

    try:
        candidate("abcdef", [(1, 4, "X"), (2, 2, "!")])
        return False
    except Exception:
        pass

    try:
        candidate("abc", [(1, 1, "X"), (1, 1, "Y")])
        return False
    except Exception:
        pass

    first = [(1, 3, "AB"), (3, 3, "!"), (5, 6, "Q")]
    second = list(reversed(first))
    try:
        if candidate("01234567", first) != candidate("01234567", second):
            return False
    except Exception:
        return False
    return True


def left_to_right(source, edits):
    out = source
    for start, end, replacement in sorted(edits, key=lambda edit: edit[0]):
        out = out[:start] + replacement + out[end:]
    return out


def reject_all_boundary_insertions(source, edits):
    for i, (s1, e1, _) in enumerate(edits):
        for s2, e2, _ in edits[i + 1 :]:
            if s1 == e1 and s2 <= s1 <= e2 and s2 != e2:
                raise ValueError("conflict")
            if s2 == e2 and s1 <= s2 <= e1 and s1 != e1:
                raise ValueError("conflict")
    return apply_edits(source, edits)


def allow_interior_insertions(source, edits):
    nonempty = [(s, e) for s, e, _ in edits if s != e]
    for i, (s1, e1) in enumerate(nonempty):
        for s2, e2 in nonempty[i + 1 :]:
            if max(s1, s2) < min(e1, e2):
                raise ValueError("overlap")
    out = source
    ordered = sorted(edits, key=lambda edit: (edit[0], edit[1] > edit[0]), reverse=True)
    for start, end, replacement in ordered:
        out = out[:start] + replacement + out[end:]
    return out


def permit_same_position_insertions(source, edits):
    out = source
    for start, end, replacement in sorted(
        edits, key=lambda edit: (edit[0], edit[1] > edit[0]), reverse=True
    ):
        out = out[:start] + replacement + out[end:]
    return out


def input_order_authority(source, edits):
    out = source
    for start, end, replacement in edits:
        out = out[:start] + replacement + out[end:]
    return out


mutants = {
    "left-to-right coordinate shift": left_to_right,
    "reject valid boundary insertion": reject_all_boundary_insertions,
    "allow interior insertion": allow_interior_insertions,
    "permit ambiguous same-position insertions": permit_same_position_insertions,
    "input declaration order authority": input_order_authority,
}

for name, mutant in mutants.items():
    assert not verify(mutant), name
assert verify(apply_edits)
print("PASS — 5/5 known-false editors rejected; accepted implementation accepted")
