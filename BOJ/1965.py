"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 상자넣기
description : Dynamic Programming
"""

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)
