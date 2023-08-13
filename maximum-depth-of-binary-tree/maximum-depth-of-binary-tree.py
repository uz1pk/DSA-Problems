from typing import Optional
from TreeNode import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Time: O(n) where n is the number of nodes in the tree
    Space: O(1) if we don't count the recursive call stack
    """
    return 0 if not root else max(maxDepth(root.left), maxDepth(root.right)) + 1
