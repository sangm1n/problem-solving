"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 서강그라운드
description : BFS
"""

import heapq


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] >= dist:
            for i, c in graph[now]:
                cost = dist + c

                if cost < distance[i] and cost <= M:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))


N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))

distance = [int(1e9) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

result = 0
for i in range(1, N+1):
    distance = [int(1e9) for _ in range(N + 1)]
    dijkstra(i)

    count = 0
    for j in range(1, N+1):
        if distance[j] != int(1e9):
            count += items[j]

    result = max(result, count)

print(result)
