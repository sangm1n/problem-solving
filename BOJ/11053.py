"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 가장 긴 증가하는 부분 수열
description : Dynamic Programming
"""

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
