"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 상자넣기
description : Dynamic Programming
"""

N = int(input())
boxes = list(map(int, input().split()))

dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if boxes[i] < boxes[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
