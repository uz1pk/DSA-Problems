from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Second Pass Implementation
    Time: O(n) where n is len(nums)
    Space: O(n) and O(1) if we don't count the output array where n is len(nums)
    """
    N = len(nums)
    output = [1] * N
    prefix_sum, suffix_sum = 1, 1

    for i in range(N):
        output[i] *= prefix_sum
        output[N - i - 1] *= suffix_sum

        prefix_sum *= nums[i]
        suffix_sum *= nums[N - i - 1]

    return output
