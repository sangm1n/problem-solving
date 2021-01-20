"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Four Squares
description : Dynamic Programming
"""

N = int(input())

dp = [0] * (N+1)
dp[0], dp[1] = 0, 1
for i in range(2, N+1):
    if i == int(i ** 0.5) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, N+1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])

print(dp[N])
