from typing import Optional
from TreeNode import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    return 0 if not root else max(maxDepth(root.left), maxDepth(root.right)) + 1
