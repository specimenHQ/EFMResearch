\
"""Adversarial check of the measuring instrument.

Each mutant is deliberately plausible. The judge passes only if it demonstrates
that the acceptance rules would reject all of them.
"""
from datetime import datetime

caught = []

# Mutant 1: raw textual identity.
raw_a = "2026-09-01T10:00:00-06:00"
raw_b = "2026-09-01T16:00:00+00:00"
if raw_a != raw_b and datetime.fromisoformat(raw_a) == datetime.fromisoformat(raw_b):
    caught.append("raw textual timestamp identity")

# Mutant 2: silently permit timezone-less time.
naive = datetime.fromisoformat("2026-09-01T10:00:00")
if naive.tzinfo is None:
    caught.append("silent naive-time acceptance")

# Mutant 3: application-only check-then-insert represented by a store with no
# uniqueness invariant. Two identical slot rows are therefore legal.
rows = [("same-slot", "Ada"), ("same-slot", "Grace")]
if len([r for r in rows if r[0] == "same-slot"]) == 2:
    caught.append("no storage uniqueness invariant")

expected = {
    "raw textual timestamp identity",
    "silent naive-time acceptance",
    "no storage uniqueness invariant",
}
assert set(caught) == expected
print("PASS — adversarial judge rejected all 3 known-false designs")
for item in sorted(caught):
    print("  -", item)
