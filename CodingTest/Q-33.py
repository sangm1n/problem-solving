"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 퇴사
description : Dynamic Programming
"""

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
result = 0
for i in range(N-1, -1, -1):
    time = table[i][0] + i

    if time < N+1:
        dp[i] = max(dp[time] + table[i][1], result)
        result = dp[i]
    else:
        dp[i] = result

print(dp[0])
