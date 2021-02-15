"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 구간 합 구하기 5
description : Prefix Sum
"""

N, M = map(int, input().split())
graph = [[0] + list(map(int, input().split())) for _ in range(N)]
graph = [[0 for _ in range(N+1)]] + graph
pos = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] += graph[i][j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] += graph[i-1][j]

for x1, y1, x2, y2 in pos:
    if x1 == 1 and y1 == 1:
        print(graph[x2][y2])
    elif x1 == 1:
        print(graph[x2][y2] - graph[x2][y1-1])
    elif y1 == 1:
        print(graph[x2][y2] - graph[x1-1][y2])
    else:
        print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])

