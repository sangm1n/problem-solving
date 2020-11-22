"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Odd Even Linked List
description : Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: ListNode) -> ListNode:
    if not head:
        return None

    odd, even = head, head.next
    second = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = second

    return head


if __name__ == '__main__':
    ex1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ex2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))

    print(oddEvenList(ex1))
    print(oddEvenList(ex2))
