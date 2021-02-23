"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
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
            for pos, c in graph[now]:
                cost = dist + c

                if cost < distance[pos]:
                    tmp[pos] = now
                    q.append((cost, pos))
                    distance[pos] = cost


X = int(input())
for x in range(1, X+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]
    distance = [int(1e9) for _ in range(M)]
    tmp = [-1 for _ in range(M)]

    for _ in range(N):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    dijkstra(0)

    result = [M-1]
    idx = M-1
    while tmp[idx] != -1:
        idx = tmp[idx]
        result.append(idx)

    result.reverse()
    if len(result) == 1:
        result = [-1]

    print('Case #{}:'.format(x), *result)
