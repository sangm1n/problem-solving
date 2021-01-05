"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 병사 배치하기
description : Dynamic Programming
"""

N = int(input())
power = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if power[i] < power[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(len(power) - max(dp))
