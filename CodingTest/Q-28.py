"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 고정점 찾기
description : Binary Search
"""


def binary_search(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if mid > arr[mid]:
        return binary_search(arr, mid + 1, end)
    elif mid < arr[mid]:
        return binary_search(arr, start, mid - 1)
    else:
        return mid


N = int(input())
arr = list(map(int, input().split()))

start, end = 0, len(arr)-1
print(binary_search(arr, start, end))
