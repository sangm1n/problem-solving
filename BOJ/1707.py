"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 이분 그래프
description : BFS
"""

from collections import deque


def bfs(x, visited):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] * (-1)
            elif visited[i] == visited[v]:
                return False
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = True
    for i in range(1, V + 1):
        if not visited[i] and not bfs(i, visited):
            flag = False
            break

    print("YES" if flag else "NO")
