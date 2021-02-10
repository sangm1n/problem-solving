"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 동전
description : Knapsack Problem
"""


def solve():
    N = int(input())
    coin = [int(x) for x in input().split()]
    coin = [0] + coin
    money = int(input())

    dp = [[0 for _ in range(money+1)] for _ in range(N+1)]
    for i in range(len(dp)):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, money+1):
            if coin[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j] + dp[i][j-coin[i]])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][money])


T = int(input())
for _ in range(T):
    solve()
