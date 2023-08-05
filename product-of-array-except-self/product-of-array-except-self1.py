from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Initial / First Pass Implementation
    Time: O(n) where n is len(nums)
    Space: O(2 * n) = O(n) where n is len(nums)
    """
    N = len(nums)
    pre, post = [1] * N, [1] * N
    prefix_sum, suffix_sum = 1, 1
    i, j = 0, N - 1

    while i != N and j != -1:
        pre[i], post[j] = prefix_sum, suffix_sum
        prefix_sum = prefix_sum * nums[i]
        suffix_sum = suffix_sum * nums[j]
        j -= 1
        i += 1

    return [pre[i] * post[i] for i in range(N)]
