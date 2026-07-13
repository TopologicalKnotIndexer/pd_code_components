from collections import Counter, defaultdict


def _sort_key(value: int | str) -> tuple[int, int | str]:
    return (0, value) if isinstance(value, int) else (1, value)


def get_components_from_pd_code(pd_code: list[list[int | str]]) -> list[list[int | str]]:
    """Return the oriented-link components represented by a valid PD code."""
    if not isinstance(pd_code, list):
        raise TypeError("pd_code must be a list")

    graph: dict[int | str, set[int | str]] = defaultdict(set)
    labels: list[int | str] = []
    label_type: type | None = None
    for crossing in pd_code:
        if not isinstance(crossing, list) or len(crossing) != 4:
            raise ValueError("every crossing must contain four labels")
        for label in crossing:
            if isinstance(label, bool) or not isinstance(label, (int, str)):
                raise TypeError("PD labels must be integers or strings")
            if label_type is None:
                label_type = type(label)
            elif type(label) is not label_type:
                raise TypeError("PD labels must use one consistent type")
            labels.append(label)
        for a, b in ((crossing[0], crossing[2]), (crossing[1], crossing[3])):
            graph[a].add(b)
            graph[b].add(a)

    if any(count != 2 for count in Counter(labels).values()):
        raise ValueError("every PD label must occur exactly twice")

    components: list[list[int | str]] = []
    seen: set[int | str] = set()
    for start in sorted(graph, key=_sort_key):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component: list[int | str] = []
        while stack:
            node = stack.pop()
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        components.append(sorted(component, key=_sort_key))
    return components
