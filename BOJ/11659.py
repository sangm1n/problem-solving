"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 구간 합 구하기 4
description : Prefix Sum
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

for i, j in prefix:
    print(arr[j] - arr[i-1])
