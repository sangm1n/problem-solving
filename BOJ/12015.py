"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 가장 긴 증가하는 부분 수열 (2)
description : Dynamic Programming
"""

from bisect import bisect_left

N = int(input())
num = list(map(int, input().split()))

dp = [num[0]]
for i in range(1, N):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        pos = bisect_left(dp, num[i])
        dp[pos] = num[i]

print(len(dp))
