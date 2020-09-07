"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Palindrome Linked List
description : Given a singly linked list, determine if it is a palindrome.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    rev = None
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


if __name__ == '__main__':
    ex1 = ListNode(1, ListNode(2))
    ex2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

    print(isPalindrome(ex1))
    print(isPalindrome(ex2))


"""
간단한 palindrome 풀이

def isPalindrome(head: ListNode) -> bool:
    q = []
    
    while head:
        q.append(head.val)
        head = head.next
    
    return q == q[::-1]
"""
