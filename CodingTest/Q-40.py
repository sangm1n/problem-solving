"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 화성 탐사
description : Shortest Path
"""

import heapq

N, M = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append((end, 1))
    graph[end].append((start, 1))

q = []
start = 1
heapq.heappush(q, (0, start))
distance[start], distance[0] = 0, 0

while q:
    dist, v = heapq.heappop(q)

    if dist > distance[v]:
        continue

    for i in graph[v]:
        vertex, cost = i[0], i[1]
        new_cost = dist + cost

        if new_cost < distance[vertex]:
            distance[vertex] = new_cost
            heapq.heappush(q, (new_cost, vertex))

max_cost = max(distance)
max_cost_idx = distance.index(max_cost)
max_cost_count = distance.count(max_cost)

print(max_cost_idx, max_cost, max_cost_count)
