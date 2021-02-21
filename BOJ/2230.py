"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수 고르기
description : Two Pointer
"""

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
left, right = 0, 0
result = int(1e9)
while left < N and right < N:
    value = arr[right] - arr[left]
    if value < M:
        right += 1
    else:
        result = min(result, value)
        left += 1

print(result)
