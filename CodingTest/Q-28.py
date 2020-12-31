"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 고정점 찾기
description : Binary Search
"""

N = int(input())
arr = list(map(int, input().split()))


def binary_search(arr, left, right):
    global flag

    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, left, mid-1)
    else:
        return binary_search(arr, mid+1, right)


result = binary_search(arr, 0, N-1)
print(-1 if result is None else result)
