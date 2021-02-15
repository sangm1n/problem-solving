"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : N번째 큰 수
description : Priority Queue
"""

import heapq

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

q = []
for i in range(N):
    for j in range(N):
        heapq.heappush(q, grid[i][j])

    while len(q) > N:
        heapq.heappop(q)

print(heapq.heappop(q))
