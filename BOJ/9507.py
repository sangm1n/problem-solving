"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Generations of Tribbles
description : Dynamic Programming
"""

T = int(input())
arr = [int(input()) for _ in range(T)]

max_num = max(arr)
dp = [0] * (max_num + 1)

dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
for i in range(4, max_num + 1):
    dp[i] = dp[i-4] + dp[i-3] + dp[i-2] + dp[i-1]

for num in arr:
    print(dp[num])
