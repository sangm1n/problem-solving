"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 플로이드
description : Shortest Path
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())

    if graph[start][end] > cost:
        graph[start][end] = cost

for i in range(1, N+1):
    for j in range(1, M+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    for j in range(1, len(graph[i])):
        print(graph[i][j], end=' ')
    print()
