"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 정확한 순위
description : Shortest Path
"""

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == N:
        result += 1

print(result)
