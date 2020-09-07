"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Merge Two Sorted Lists
description : Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    merge_list = []

    while l1:
        merge_list.append(l1.val)
        l1 = l1.next
    while l2:
        merge_list.append(l2.val)
        l2 = l2.next
    merge_list.sort()

    result = None

    for i in range(len(merge_list)):
        if i == 0:
            result = ListNode(merge_list[i])
        else:
            new_node = ListNode(merge_list[i])
            current_node = result
            while current_node.next:
                current_node = current_node.next
            result = new_node

    return result


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    print(mergeTwoLists(l1, l2))
