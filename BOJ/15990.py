"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 1, 2, 3 더하기 5
description : Dynamic Programming
"""

import sys
input = sys.stdin.readline

dp = [[0 for _ in range(4)] for _ in range(100000+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, 100000+1):
    for j in range(1, 3+1):
        if j < 3:
            dp[i][j] = (dp[i-j][3-j] + dp[i-j][3]) % 1000000009
        else:
            dp[i][j] = (dp[i-j][1] + dp[i-j][2]) % 1000000009


def solve():
    N = int(input())

    print(sum(dp[N]) % 1000000009)


T = int(input())
for _ in range(T):
    solve()
