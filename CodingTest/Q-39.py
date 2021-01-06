"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 화성 탐사
description : Shortest Path
"""

import heapq
INF = int(1e9)

T = int(input())
for _ in range(T):
    N = int(input())
    mars = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    x, y = 0, 0
    q = [(mars[x][y], x, y)]
    distance[x][y] = mars[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        dist, x, y = heapq.heappop(q)

        if dist > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue

            cost = mars[nx][ny] + dist
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                q.append((cost, nx, ny))

    print(distance[N-1][N-1])
