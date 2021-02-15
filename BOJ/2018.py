"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수들의 합 5
description : Two Pointer
"""

N = int(input())

i, j = 1, 2
total = 3
result = 0
while i <= N-1 and j <= N:
    if total < N:
        j += 1
        total += j
    else:
        if total == N:
            result += 1
        i += 1
        total -= i-1

print(result + 1)
