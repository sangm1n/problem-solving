"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 로봇 조종하기
description : Dynamic Programming
"""

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-int(1e9) for _ in range(M+2)] for _ in range(N+1)] for _ in range(3)]
dp[0][1][0], dp[1][1][0], dp[2][1][0] = 0, 0, 0

for i in range(1, M+1):
    for k in range(3):
        dp[k][1][i] = dp[k][1][i-1] + graph[0][i-1]

for i in range(2, N+1):
    for j in range(1, M+1):
        dp[0][i][j] = max(dp[0][i][j], dp[0][i-1][j] + graph[i-1][j-1], dp[0][i][j-1] + graph[i-1][j-1])
    for j in range(M, -1, -1):
        dp[1][i][j] = max(dp[1][i][j], dp[1][i-1][j] + graph[i-1][j-1], dp[1][i][j+1] + graph[i-1][j-1])

    for j in range(1, M+1):
        dp[2][i][j] = max(dp[0][i][j], dp[1][i][j])

    dp[0][i] = dp[2][i]
    dp[1][i] = dp[2][i]

print(dp[2][N][M])
