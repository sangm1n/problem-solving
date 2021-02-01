"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연속합
description : Dynamic Programming
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = arr[0]

for i in range(2, N+1):
    dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])

print(max(dp[1:]))
