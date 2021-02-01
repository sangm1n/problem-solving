"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : BABBA
description : Dynamic Programming
"""

K = int(input())

dp = [(0, 0)] * (K+1)

if K == 1:
    print(0, 1)
elif K == 2:
    print(1, 1)
else:
    dp[1], dp[2] = (0, 1), (1, 1)

    for i in range(3, K+1):
        dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])

    print(*dp[K])
