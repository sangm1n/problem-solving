"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 앱
description : Knapsack Problem
"""

import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
byte = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]

total = sum(cost)
dp = [[0 for _ in range(total+1)] for _ in range(N+1)]

result = math.inf
for i in range(1, N+1):
    for j in range(1, total+1):
        if j >= cost[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + byte[i-1])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            result = min(result, j)

print(result)
