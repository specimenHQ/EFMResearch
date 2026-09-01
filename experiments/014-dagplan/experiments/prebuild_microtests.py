from itertools import permutations


def kahn_consumed(nodes, edges):
    indegree = {node: 0 for node in nodes}
    outgoing = {node: [] for node in nodes}
    for dependency, task in edges:
        outgoing[dependency].append(task)
        indegree[task] += 1
    ready = sorted(node for node, degree in indegree.items() if degree == 0)
    seen = []
    while ready:
        node = ready.pop(0)
        seen.append(node)
        for dependent in outgoing[node]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)
                ready.sort()
    return seen


def naive_live_stages(nodes, edges):
    indegree = {node: 0 for node in nodes}
    outgoing = {node: [] for node in nodes}
    for dependency, task in edges:
        outgoing[dependency].append(task)
        indegree[task] += 1
    ready = sorted(node for node, degree in indegree.items() if degree == 0)
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
        stages.append(stage)
        ready = []
    return stages


def frozen_frontier_stages(nodes, edges):
    indegree = {node: 0 for node in nodes}
    outgoing = {node: [] for node in nodes}
    for dependency, task in edges:
        outgoing[dependency].append(task)
        indegree[task] += 1
    frontier = sorted(node for node, degree in indegree.items() if degree == 0)
    stages = []
    while frontier:
        current = frontier
        stages.append(current)
        next_frontier = []
        for node in current:
            for dependent in outgoing[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_frontier.append(dependent)
        frontier = sorted(next_frontier)
    return stages


def staged_plan(declarations):
    ids = [task_id for task_id, _ in declarations]
    indegree = {task_id: 0 for task_id in ids}
    outgoing = {task_id: [] for task_id in ids}
    for task_id, dependencies in declarations:
        for dependency in dependencies:
            outgoing[dependency].append(task_id)
            indegree[task_id] += 1
    frontier = sorted(task_id for task_id, degree in indegree.items() if degree == 0)
    stages = []
    while frontier:
        current = frontier
        stages.append(tuple(current))
        next_frontier = []
        for node in current:
            for dependent in outgoing[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_frontier.append(dependent)
        frontier = sorted(next_frontier)
    return tuple(stages)


# A1: Kahn consumption distinguishes controlled acyclic/cyclic fixtures.
assert kahn_consumed(["A", "B", "C"], [("A", "B"), ("B", "C")]) == ["A", "B", "C"]
assert kahn_consumed(["A", "B"], [("A", "B"), ("B", "A")]) == []
print("A1 PASS — cyclic fixture leaves nodes unconsumed")

# A2: mutating the current frontier collapses a dependency level.
naive = naive_live_stages(["A", "B", "C"], [("A", "C")])
frozen = frozen_frontier_stages(["A", "B", "C"], [("A", "C")])
assert naive == [["A", "B", "C"]]
assert frozen == [["A", "B"], ["C"]]
print("A2 FALSIFIED naive live-frontier staging — C joined prerequisite A's stage")

# A3: sorted frozen frontiers survive every declaration permutation.
fixture = [("C", ["A", "B"]), ("A", []), ("D", ["C"]), ("B", [])]
plans = {staged_plan(p) for p in permutations(fixture)}
assert plans == {(("A", "B"), ("C",), ("D",))}
print("A3 PASS — 24 declaration permutations produced one plan")

# A4: ordinary dict construction silently overwrites duplicate task IDs.
duplicate_declarations = [("A", ["X"]), ("A", ["Y"])]
collapsed = {task_id: dependencies for task_id, dependencies in duplicate_declarations}
assert collapsed == {"A": ["Y"]}
print("A4 CONFIRMED hazard — duplicate task declaration was silently overwritten")

# A5: permissive setdefault construction invents an undeclared dependency node.
graph = {}
for task_id, dependencies in [("B", ["A"])]:
    graph.setdefault(task_id, [])
    for dependency in dependencies:
        graph.setdefault(dependency, []).append(task_id)
assert sorted(graph) == ["A", "B"]
print("A5 CONFIRMED hazard — undeclared dependency A became a graph node")

# A6: list indegree plus set adjacency can produce a false residual indegree.
dependencies = {"A": [], "B": ["A", "A"]}
indegree = {task_id: len(deps) for task_id, deps in dependencies.items()}
outgoing = {task_id: set() for task_id in dependencies}
for task_id, deps in dependencies.items():
    for dependency in deps:
        outgoing[dependency].add(task_id)
ready = ["A"]
seen = []
while ready:
    node = ready.pop(0)
    seen.append(node)
    for dependent in outgoing[node]:
        indegree[dependent] -= 1
        if indegree[dependent] == 0:
            ready.append(dependent)
assert seen == ["A"] and indegree["B"] == 1
print("A6 CONFIRMED hazard — duplicate dependency left false residual indegree")
