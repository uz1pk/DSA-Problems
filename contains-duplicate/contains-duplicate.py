from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)
    """
    return len(set(nums)) != len(nums)
