"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수들의 합 2
description : Two Pointer
"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, 1
result = 0
while i <= N-1 and j <= N:
    if sum(arr[i:j+1]) > M:
        i += 1
    elif sum(arr[i:j+1]) < M:
        j += 1
    else:
        i += 1
        j += 1
        result += 1

print(result)
