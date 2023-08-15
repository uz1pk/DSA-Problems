from typing import Optional
from ListNode import ListNode


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy_small = small_ref = ListNode()
    dummy_big = big_ref = ListNode()

    iterator = head
    while iterator:
        if iterator.val < x:
            dummy_small.next = ListNode(iterator.val)
            dummy_small = dummy_small.next
        else:
            dummy_big.next = ListNode(iterator.val)
            dummy_big = dummy_big.next
        iterator = iterator.next

    dummy_small.next = big_ref.next
    return small_ref.next if small_ref.next else head
