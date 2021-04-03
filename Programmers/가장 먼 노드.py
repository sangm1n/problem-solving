"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 가장 먼 노드
description : Graph
"""

from collections import deque


def find_distance(v, graph):
    distance = [0] * len(graph)
    visited = [0] * len(graph)
    visited[v] = 1

    q = deque()
    q.append(v)

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                distance[i] += distance[now] + 1

    return distance


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = find_distance(1, graph)
    max_dist = max(dist)

    return dist.count(max_dist)


if __name__ == '__main__':
    n = 6
    edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    result = solution(n, edges)
    print(result)
