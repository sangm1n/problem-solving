"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 사탕 가게
description : Knapsack Problem
"""

import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n, m = int(n), int(m * 100 + 0.5)

    if n == 0 and m == 0:
        break

    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)

        for i in range(p, m+1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(dp[m])
