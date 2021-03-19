"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 최단경로
description : Shortest Path
"""

import heapq


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        weight, v = heapq.heappop(q)

        if distance[v] >= weight:
            for i, cost in graph[v]:
                new_cost = weight + cost

                if distance[i] > new_cost:
                    distance[i] = new_cost
                    heapq.heappush(q, (new_cost, i))


INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)

dijkstra(start, distance)
[print('INF' if dist == INF else dist) for dist in distance[1:]]
