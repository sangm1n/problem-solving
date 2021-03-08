"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연결 요소의 개수
description : DFS
"""

import sys
sys.setrecursionlimit(10**6)


def dfs(start, visited):
    visited[start] = True

    for v in graph[start]:
        if not visited[v]:
            dfs(v, visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited)
        count += 1

print(count)
