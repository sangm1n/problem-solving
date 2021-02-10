"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 벼락치기
description : Knapsack Problem
"""

N, T = map(int, input().split())
time, score = [], []
for i in range(N):
    K, S = map(int, input().split())
    time.append(K)
    score.append(S)

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, T+1):
        if j >= time[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + score[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])
