"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 1로 만들기
description : Dynamic Programming
"""

N = int(input())

dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])
