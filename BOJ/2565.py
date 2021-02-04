"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 전깃줄
description : Dynamic Programming
"""

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

line.sort(key=lambda x: x[0])

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
