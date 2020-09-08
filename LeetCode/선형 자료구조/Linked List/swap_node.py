"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Swap Nodes in Pairs
description : Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next

    return root.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print(swapPairs(head))
