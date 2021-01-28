"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 암기왕
description : Sorting
"""

import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


T = int(input())
for _ in range(T):
    one = int(input())
    one_note = list(map(int, input().split()))
    two = int(input())
    two_note = list(map(int, input().split()))

    one_note.sort()

    for target in two_note:
        print(0 if binary_search(one_note, target, 0, one-1) is None else 1)
