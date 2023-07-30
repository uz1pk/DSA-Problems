import heapq
from typing import List, Optional
from ListNode import ListNode


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time: O(n log n) where n is the total number of nodes in all lists
        iterating through heap + heappop results in O(n log n) asymptotic time complexity
    Space: O(n) where n is the total number of nodes in all lists
    """
    head = dummy = ListNode()
    heap = []

    for node in lists:
        temp_head = node
        while temp_head:
            heap.append(temp_head.val)
            temp_head = temp_head.next

    heapq.heapify(heap)

    while heap:
        node = ListNode(heapq.heappop(heap))
        dummy.next = node
        dummy = dummy.next

    return head.next
