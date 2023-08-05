from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    Initial / First Pass Implementation
    Time: O(n log n) where n is len(nums)
    Space: O(n) where n is len(nums)
    """
    unique_nums = sorted(set(nums))
    length = longest_seq = 0
    for i, value in enumerate(unique_nums):
        if unique_nums[i - 1] + 1 != value:
            length = 0
        length += 1
        longest_seq = max(length, longest_seq)
    return longest_seq
