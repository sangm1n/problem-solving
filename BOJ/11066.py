"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 파일 합치기
description : Dynamic Programming
"""

import math


def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(j, -1, -1):
            if i == j:
                continue

            small = math.inf
            for k in range(j-i):
                small = min(small, dp[i][i+k] + dp[i+k+1][j])
            dp[i][j] = small + sum(arr[i:j+1])

    print(dp[0][n-1])


t = int(input())
for _ in range(t):
    solve()
