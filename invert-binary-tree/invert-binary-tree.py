from typing import Optional
from TreeNode import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time: O(n) where n is the number of nodes in the tree
    Space: O(1) if we don't count the recursive call stack
    """
    if not root:
        return
    root.left, root.right = root.right, root.left
    invertTree(root.right)
    invertTree(root.left)
    return root