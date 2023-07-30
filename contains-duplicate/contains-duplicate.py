from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    First Pass
    O(n) where n is len(nums)
    """
    return len(set(nums)) != len(nums)