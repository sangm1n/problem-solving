"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 평범한 배낭
description : Knapsack Problem
"""

N, K = map(int, input().split())
weight, value = [], []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

weight, value = [0] + weight, [0] + value

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
