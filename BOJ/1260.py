"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : DFS와 BFS
description : Graph
"""

from collections import deque


def dfs(visited, start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(visited, i)


def bfs(visited, start):
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

for g in graph:
    g.sort()

visited = [False] * (N+1)
dfs(visited, V)
print()
visited = [False] * (N+1)
bfs(visited, V)
