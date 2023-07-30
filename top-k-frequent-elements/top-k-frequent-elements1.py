from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Initial / First Pass Implementation
    """
    frequencies = Counter(nums)
    sorted_frequencies_list = sorted([tuple((key,val)) for key,val in frequencies.items()], key=lambda x: x[1], reverse=True)
    return [sorted_frequencies_list[i][0] for i in range(k)]