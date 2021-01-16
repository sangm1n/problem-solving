"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연결 요소의 개수
description : Graph
"""

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(visited, graph, v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(visited, graph, i)


visited = [False] * (N+1)
count = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    dfs(visited, graph, i)
    count += 1

print(count)
