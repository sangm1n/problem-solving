"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 트리의 부모 찾기
description : DFS
"""


def dfs(x, p, visited):
    global result

    stack = []
    stack.append((x, p))
    visited[x] = True

    while stack:
        v, parent = stack.pop()
        result[v] = parent

        for i in graph[v]:
            if not visited[i]:
                stack.append((i, v))
                visited[i] = True


N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = [0] * (N+1)

dfs(1, 0, visited)
[print(result[i]) for i in range(2, N+1)]
