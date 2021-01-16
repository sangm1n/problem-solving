"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : ATM
description : Dynamic Programming
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i-1] + arr[i]

print(sum(dp))
