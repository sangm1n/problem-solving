"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 전보
description : Dijkstra Algorithm
"""

import heapq


def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] >= dist:
            for goal, cost in graph[now]:
                new_dist = dist + cost
                if distance[goal] > new_dist:
                    distance[goal] = new_dist
                    heapq.heappush(q, (new_dist, goal))


N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

distance = [int(1e9)] * (N+1)
dijkstra(C, distance, graph)

count, result = 0, 0
for i in range(1, N+1):
    if distance[i] < int(1e9):
        count += 1
        result = max(result, distance[i])

print(count, result)
