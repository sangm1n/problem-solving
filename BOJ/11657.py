"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 타임머신
description : 플로이드-워셜
"""

INF = int(1e9)


def ford(start):
    global cycle
    distance[start] = 0

    for i in range(N):
        for j in range(1, N+1):
            for now, cost in graph[j]:
                if distance[j] <= INF and distance[now] > distance[j] + cost:
                    distance[now] = distance[j] + cost
                    if i == N-1:
                        cycle = True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

cycle = False
ford(1)

if cycle:
    print(-1)
else:
    for dist in distance[2:]:
        print(-1 if dist == INF else dist)
