import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dagplan import plan_stages


def verify(candidate):
    if candidate([("C", ["A"]), ("A", []), ("B", [])]) != (("A", "B"), ("C",)):
        return False

    first = [("C", ["A", "B"]), ("A", []), ("B", [])]
    second = [("B", []), ("C", ["A", "B"]), ("A", [])]
    if candidate(first) != candidate(second):
        return False

    try:
        candidate([("A", []), ("A", [])])
        return False
    except Exception:
        pass

    try:
        candidate([("B", ["A"])])
        return False
    except Exception:
        pass

    try:
        candidate([("A", ["B"]), ("B", ["A"])])
        return False
    except Exception:
        pass

    return True


def live_frontier(declarations):
    ids = [task for task, _ in declarations]
    indegree = {task: 0 for task in ids}
    outgoing = {task: [] for task in ids}
    for task, dependencies in declarations:
        for dependency in dependencies:
            outgoing[dependency].append(task)
            indegree[task] += 1
    ready = sorted(task for task, degree in indegree.items() if degree == 0)
    stages = []
    while ready:
        stage = []
        i = 0
        while i < len(ready):
            node = ready[i]
            i += 1
            stage.append(node)
            for dependent in outgoing[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    ready.append(dependent)
        stages.append(tuple(stage))
        ready = []
    return tuple(stages)


def input_order(declarations):
    ids = [task for task, _ in declarations]
    rank = {task: i for i, task in enumerate(ids)}
    indegree = {task: 0 for task in ids}
    outgoing = {task: [] for task in ids}
    for task, dependencies in declarations:
        for dependency in dependencies:
            outgoing[dependency].append(task)
            indegree[task] += 1
    ready = [task for task in ids if indegree[task] == 0]
    stages = []
    used = 0
    while ready:
        current = tuple(ready)
        stages.append(current)
        used += len(current)
        next_frontier = []
        for node in current:
            for dependent in outgoing[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_frontier.append(dependent)
        ready = sorted(next_frontier, key=rank.get)
    if used != len(ids):
        raise ValueError("cycle")
    return tuple(stages)


def overwrite_duplicates(declarations):
    collapsed = {task: list(dependencies) for task, dependencies in declarations}
    return plan_stages(collapsed.items())


def invent_unknown(declarations):
    tasks = {task: list(dependencies) for task, dependencies in declarations}
    for dependencies in list(tasks.values()):
        for dependency in dependencies:
            tasks.setdefault(dependency, [])
    return plan_stages(tasks.items())


def ignore_cycle(declarations):
    ids = [task for task, _ in declarations]
    indegree = {task: 0 for task in ids}
    outgoing = {task: [] for task in ids}
    for task, dependencies in declarations:
        for dependency in dependencies:
            if dependency in outgoing:
                outgoing[dependency].append(task)
                indegree[task] += 1
    ready = sorted(task for task, degree in indegree.items() if degree == 0)
    stages = []
    while ready:
        current = tuple(ready)
        stages.append(current)
        next_frontier = []
        for node in current:
            for dependent in outgoing[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_frontier.append(dependent)
        ready = sorted(next_frontier)
    return tuple(stages)


mutants = {
    "live-frontier stage collapse": live_frontier,
    "input declaration order authority": input_order,
    "duplicate task last-write-wins": overwrite_duplicates,
    "unknown dependency invention": invent_unknown,
    "cycle silently omitted": ignore_cycle,
}

for name, mutant in mutants.items():
    assert not verify(mutant), name
assert verify(plan_stages)
print("PASS — 5/5 known-false planners rejected; accepted implementation accepted")
