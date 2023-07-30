from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)
    """
    complement_dict = {}
    for i, num in enumerate(nums):
        if num in complement_dict:
            return [complement_dict[num], i]
        complement_dict[target - num] = i
