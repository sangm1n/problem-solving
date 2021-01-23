"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연결 요소의 개수
description : BFS
"""

from collections import deque


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
