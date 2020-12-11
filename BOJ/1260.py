"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
"""

import sys
from collections import deque
input = sys.stdin.readline


def dfs(graph, v, visited):
    global dfs_result
    visited[v] = True

    dfs_result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    global bfs_result
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_result.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

graph = [[] for x in range(N+1)]

for _ in range(M):
    idx, value = map(int, input().split())
    graph[idx].append(value)
    graph[value].append(idx)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited)

visited = [False] * (N + 1)
bfs_result = []
bfs(graph, V, visited)

[print(val, end=' ') for val in dfs_result]
print()
[print(val, end=' ') for val in bfs_result]
