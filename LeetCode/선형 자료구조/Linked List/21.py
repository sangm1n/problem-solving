"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    q = deque()

    while True:
        if l1 is None and l2 is None:
            break
        elif l1 and l2:
            if l1.val >= l2.val:
                q.append(l2.val)
                l2 = l2.next
            else:
                q.append(l1.val)
                l1 = l1.next
        elif l1 is None and l2 is not None:
            q.append(l2.val)
            l2 = l2.next
        elif l1 is not None and l2 is None:
            q.append(l1.val)
            l1 = l1.next

    answer = None
    for i in range(len(q)):
        if i == 0:
            answer = ListNode(q.popleft())
        else:
            new_node = ListNode(q.popleft())
            current = answer
            while current.next:
                current = current.next
            current.next = new_node

    return answer


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

print(mergeTwoLists(l1, l2))