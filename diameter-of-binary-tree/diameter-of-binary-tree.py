from typing import Optional
from TreeNode import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Time: O(n) where n is the number of nodes in the tree
    Space: O(1) if we don't count the recursive call stack
    """
    if not root:
        return 0

    def dfs(current_root):
        if not current_root:
            return (0, 0)
        l_edges, l_diameter = dfs(current_root.left) if current_root.left else (0, 0)
        r_edges, r_diameter = dfs(current_root.right) if current_root.right else (0, 0)
        if current_root.left:
            l_edges += 1
        if current_root.right:
            r_edges += 1

        return (max(l_edges, r_edges), max(l_edges + r_edges, r_diameter, l_diameter))

    return dfs(root)[1]
