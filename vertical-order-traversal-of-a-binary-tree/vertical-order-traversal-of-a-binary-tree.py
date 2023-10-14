from collections import defaultdict
from typing import List, Optional, Tuple, Dict
from TreeNode import TreeNode


def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    nodes_each_depth: Dict[int, List[Tuple[Optional[TreeNode], int]]] = defaultdict(
        list
    )

    def dfs(n: Optional[TreeNode], x: int, y: int):
        if not n:
            return
        nonlocal nodes_each_depth
        dfs(n.left, x + 1, y - 1)
        dfs(n.right, x + 1, y + 1)
        nodes_each_depth[y].append((n, x))

    dfs(root, 0, 0)
    keys = sorted(nodes_each_depth.keys())
    return [
        map(
            lambda y: y[0].val,
            sorted(nodes_each_depth[k], key=lambda x: (x[1], x[0].val)),
        )
        for k in keys
    ]
