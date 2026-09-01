from functools import lru_cache

fixture = {
    "A": (),
    "B": (),
    "C": ("A",),
    "D": ("A", "B"),
    "E": ("C", "D"),
}


@lru_cache(None)
def independent_depth(task):
    dependencies = fixture[task]
    return 0 if not dependencies else 1 + max(independent_depth(dep) for dep in dependencies)


by_depth = {}
for task in fixture:
    by_depth.setdefault(independent_depth(task), []).append(task)

stages = tuple(tuple(sorted(by_depth[level])) for level in sorted(by_depth))
assert stages == (("A", "B"), ("C", "D"), ("E",))
print("PASS — independent longest-dependency-depth oracle gives ((A,B),(C,D),(E))")
