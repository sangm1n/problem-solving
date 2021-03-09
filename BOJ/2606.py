"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 바이러스
description : BFS
"""

from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(visited[1:].count(True) - 1)
