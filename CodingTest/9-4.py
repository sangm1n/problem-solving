"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 미래 도시
description : 플로이드-워셜
"""

N, M = map(int, input().split())

graph = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

dist = graph[1][K] + graph[K][X]
print(-1 if dist > int(1e9) else dist)
