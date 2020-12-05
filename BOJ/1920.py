"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))


def binary_search(value, arr, start, end):
    mid = (start + end) // 2

    if start > end:
        return 0

    if arr[mid] < value:
        return binary_search(value, arr, mid + 1, end)
    elif arr[mid] > value:
        return binary_search(value, arr, start, mid - 1)
    else:
        return 1


for n in num:
    start, end = 0, N-1
    print(binary_search(n, A, start, end))
