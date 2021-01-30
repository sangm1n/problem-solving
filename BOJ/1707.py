"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 이분 그래프
description : BFS
"""

from collections import deque


def bfs(n, visited, check):
    q = deque()
    q.append(n)
    visited[n] = True
    check[n] = 1

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                check[nx] = check[x] * -1
                visited[nx] = True
            elif check[nx] == check[x]:
                return False

    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (V+1)
    check = [0] * (V+1)

    flag = True
    for i in range(1, len(graph)):
        if not visited[i] and not bfs(i, visited, check):
            flag = False

    print("YES" if flag else "NO")
