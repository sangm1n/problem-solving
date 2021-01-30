"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 입국심사
description : Binary Search
"""

import sys
input = sys.stdin.readline


def binary_search(left, right):
    result = 0
    while left <= right:
        mid = (left + right) // 2

        people = 0
        for t in time:
            people += mid // t

        if people < M:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    return result


N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]

left, right = 0, max(time) * M
print(binary_search(left, right))
