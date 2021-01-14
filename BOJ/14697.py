"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 방 배정하기
description : Back-tracking
"""

A, B, C, N = map(int, input().split())
dp = [0] * (N+1)

dp[A] = dp[B] = dp[C] = 1

for i in range(A, N+1):
    for j in [A, B, C]:
        if i >= j and dp[i-j] != 0:
            dp[i] = 1

print(dp[N])
