"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Reverse Linked List 2
description : Reverse a linked list from position m to n. Do it in one-pass.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    for _ in range(m-1):
        start = start.next
    end = start.next

    for _ in range(n-m):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp

    return root.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    m, n = 2, 4

    print(reverseBetween(head, m, n))
