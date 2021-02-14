"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 양팔저울
description : Knapsack Problem
"""

N = int(input())
weight = list(map(int, input().split()))
M = int(input())
marble = list(map(int, input().split()))

dp = [False for _ in range(40001)]
dp[0] = True

for i in range(N):
    tmp = [False for _ in range(40001)]
    for j in range(40000, -1, -1):
        if dp[j]:
            tmp[j] = True
            tmp[j + weight[i]] = True
            if weight[i] - j >= 0:
                tmp[weight[i] - j] = True
            if j - weight[i] >= 0:
                tmp[j - weight[i]] = True
    dp = tmp[:]

for m in marble:
    if dp[m]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
