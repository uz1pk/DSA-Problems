from collections import deque
from typing import List
from Node import Node


def levelOrder(root: Node) -> List[List[int]]:
    """
    Time: O(n) - n is the number of nodes
    Space: O(n) - n is the number of nodes
    """
    queue = deque() if not root else deque([(root, 0)])
    result = []

    while queue:
        node, level = queue.popleft()

        if level == len(result):
            result.append([])
        result[level].append(node.val)

        for child in node.children:
            queue.append((child, level + 1))
    return result
