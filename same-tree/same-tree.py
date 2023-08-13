from typing import Optional
from TreeNode import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Time: O(n * m) where n is the number of nodes in the first tree and m is the number of nodes in the second tree
    Space: O(1) if we don't count the recursive call stack
    """
    if not p and not q:
        return True
    elif not p or not q:
        return False
    return (
        p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    )
