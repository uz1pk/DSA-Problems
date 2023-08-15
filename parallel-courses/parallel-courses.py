from collections import deque
from typing import List


def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    """
    Time: O(n + e) where e is the number of edges in relations and n is the number of courses
    Space: O(n + e) where e is the number of edges in relations and n is the number of courses
    """

    # building the dependency graph
    incoming = {x: set() for x in range(1, n + 1)}
    for in_node, out in relations:
        incoming[out].add(in_node)

    num_days = -1
    visited = set()
    queue = deque([(x, 1) for x in incoming if len(incoming[x]) == 0])

    # BFS
    while queue:
        course, days = queue.popleft()
        if course in visited:
            continue
        visited.add(course)
        num_days = max(days, num_days)

        for key in incoming:
            if course in incoming[key]:
                incoming[key].remove(course)
            if len(incoming[key]) == 0:
                queue.append((key, days + 1))

    # if all courses are visited, return the minimum number of days
    return num_days if len(visited) == n else -1
