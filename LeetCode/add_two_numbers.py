"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Add Two Numbers
description : You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_list, l2_list = [], []

    while l1:
        l1_list.append(l1.val)
        l1 = l1.next
    while l2:
        l2_list.append(l2.val)
        l2 = l2.next

    l1_list.reverse()
    l2_list.reverse()

    total = int(''.join(map(str, l1_list))) + int(''.join(map(str, l2_list)))
    total = list(str(total))
    total = list(map(int, total))
    total.reverse()

    result = None
    for i in range(len(total)):
        if i == 0:
            result = ListNode(total[i])
        else:
            new_node = ListNode(total[i])
            current_node = result
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    return result


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print(addTwoNumbers(l1, l2))
