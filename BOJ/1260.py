"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : DFS와 BFS
description : Graph
"""

from collections import deque


def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

[x.sort() for x in graph]

visited = [False] * (N+1)
dfs(V, visited)
print()
visited = [False] * (N+1)
bfs(V, visited)
