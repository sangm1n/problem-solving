"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 못생긴 수
description : Dynamic Programming
"""

N = int(input())
dp = [0] * N
dp[0] = 1

idx2, idx3, idx5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

for i in range(1, N):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        idx2 += 1
        next2 = dp[idx2] * 2
    if dp[i] == next3:
        idx3 += 1
        next3 = dp[idx3] * 3
    if dp[i] == next5:
        idx5 += 1
        next5 = dp[idx5] * 5

print(dp[N-1])
