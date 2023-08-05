from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    Second Pass Implementation
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)
    """
    unique_nums = set(nums)
    length = 0

    for num in unique_nums:
        if num - 1 not in unique_nums:
            curr, curr_len = num, 1

            while curr + 1 in unique_nums:
                curr += 1
                curr_len += 1
            length = max(length, curr_len)

    return length
