"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 최소비용 구하기
description : Dijkstra Algorithm
"""

import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] >= dist:
            for pos, c in bus[now]:
                cost = dist + c

                if cost < distance[pos]:
                    q.append((cost, pos))
                    distance[pos] = cost


N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    bus[a].append((b, cost))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
