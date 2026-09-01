from __future__ import annotations


class PlanError(ValueError):
    pass


class DuplicateTaskError(PlanError):
    pass


class UnknownDependencyError(PlanError):
    pass


class DuplicateDependencyError(PlanError):
    pass


class CycleError(PlanError):
    pass


def plan_stages(declarations):
    """Return deterministic dependency stages as a tuple of tuples."""
    entries = []
    seen_ids = set()

    for task_id, dependencies in declarations:
        if not isinstance(task_id, str):
            raise TypeError("task_id must be a string")
        if task_id in seen_ids:
            raise DuplicateTaskError(f"duplicate task id: {task_id!r}")
        seen_ids.add(task_id)

        deps = tuple(dependencies)
        if any(not isinstance(dep, str) for dep in deps):
            raise TypeError("dependency ids must be strings")
        if len(set(deps)) != len(deps):
            raise DuplicateDependencyError(
                f"task {task_id!r} repeats a dependency"
            )
        entries.append((task_id, deps))

    declared_ids = {task_id for task_id, _ in entries}

    for task_id, dependencies in entries:
        unknown = sorted(dep for dep in dependencies if dep not in declared_ids)
        if unknown:
            raise UnknownDependencyError(
                f"task {task_id!r} references unknown dependencies: {unknown!r}"
            )

    indegree = {task_id: 0 for task_id in declared_ids}
    outgoing = {task_id: [] for task_id in declared_ids}

    for task_id, dependencies in entries:
        indegree[task_id] = len(dependencies)
        for dependency in dependencies:
            outgoing[dependency].append(task_id)

    frontier = sorted(
        task_id for task_id, degree in indegree.items() if degree == 0
    )
    stages = []
    consumed = 0

    while frontier:
        current = tuple(frontier)
        stages.append(current)
        consumed += len(current)

        next_frontier = []
        for task_id in current:
            for dependent in outgoing[task_id]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_frontier.append(dependent)
        frontier = sorted(next_frontier)

    if consumed != len(declared_ids):
        remaining = sorted(
            task_id for task_id, degree in indegree.items() if degree > 0
        )
        raise CycleError(f"dependency cycle among tasks: {remaining!r}")

    return tuple(stages)
