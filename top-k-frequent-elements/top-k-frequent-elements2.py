from collections import Counter
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Second Pass Implementation
    Time: O(n log k) where n is len(nums) and k is # of top k value
    Space: O(n) where n is len(nums)
    """
    frequencies, heap = Counter(nums), []
    for i in frequencies.keys():
        heapq.heappush(heap, (frequencies[i], i))
    frequencies = heapq.nlargest(k, heap)
    return [j for _, j in frequencies]
