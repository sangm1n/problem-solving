"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수강 과목
description : Knapsack Problem
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

importance, time = [], []
for _ in range(K):
    I, T = map(int, input().split())
    importance.append(I)
    time.append(T)

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        if j >= time[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + importance[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[K][N])
