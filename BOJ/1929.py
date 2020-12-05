"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""

import math
import sys

M, N = map(int, sys.stdin.readline().split())


def prime(start, end):
    arr = [False] * (end + 1)
    arr[0], arr[1] = True, True

    for i in range(2, int(math.sqrt(end))+1):
        if arr[i]:
            continue

        for j in range(2*i, end+1, i):
            arr[j] = True

    for i in range(2, end+1):
        if not arr[i] and i >= start:
            print(i)


prime(M, N)
