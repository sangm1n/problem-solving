"""
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.
"""
from collections import deque


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode):
    q = deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


a = ListNode(1, ListNode(2))
b = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

print(isPalindrome(a))
print(isPalindrome(b))


"""
Runner 기법 이용

def isPalindrome(head: ListNode):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev
"""