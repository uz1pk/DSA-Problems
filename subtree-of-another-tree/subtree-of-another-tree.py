from typing import Optional
from TreeNode import TreeNode


def isSameTree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if not root and not sub_root:
        return True
    if (not root or not sub_root) or root.val != sub_root.val:
        return False
    return isSameTree(root.left, sub_root.left) and isSameTree(
        root.right, sub_root.right
    )


def isSubtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    has_same = False

    def dfs(node):
        nonlocal has_same
        if node and sub_root and node.val == sub_root.val:
            has_same = has_same or isSameTree(node, sub_root)
        if node:
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return has_same
