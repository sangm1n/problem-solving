"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 특정 거리의 도시 찾기
description : BFS
"""

import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [int(1e9) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijkstra(X)

flag = False
for i in range(1, N+1):
    if distance[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
