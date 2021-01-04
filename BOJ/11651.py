"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 좌표 정렬하기 2
description : Sorting
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))
for x, y in arr:
    print(x, y)
    