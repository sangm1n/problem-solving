"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 2 x n 타일링
description : Dynamic Programming
"""

N = int(input())

dp = [0] * (N+1)

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp[1], dp[2] = 1, 2

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N] % 10007)
