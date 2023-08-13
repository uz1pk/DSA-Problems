from typing import Optional
from TreeNode import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    balance = True

    def dfs(current_node):
        if not current_node:
            return 0
        nonlocal balance
        left, right = dfs(current_node.left), dfs(current_node.right)
        balance = left - right >= -1 and left - right <= 1 and balance
        return max(left, right) + 1

    dfs(root)
    return balance
