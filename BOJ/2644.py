"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 촌수계산
description : BFS
"""

from collections import deque


def bfs(n):
    q = deque()
    q.append((n, 0))
    visited[n] = True

    while q:
        v, cnt = q.popleft()

        if v == b:
            return cnt

        for x in graph[v]:
            if not visited[x]:
                q.append((x, cnt + 1))
                visited[x] = True

    return -1


N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

visited = [False] * (N+1)

print(bfs(a))
