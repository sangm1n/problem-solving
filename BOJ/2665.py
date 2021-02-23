"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 미로만들기
description : Dijkstra Algorithm
"""

import heapq
INF = int(1e9)


def dijkstra(i, j):
    q = []
    heapq.heappush(q, (0, i, j))
    visited[i][j] = True

    while q:
        count, x, y = heapq.heappop(q)

        if x == N-1 and y == N-1:
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maze[nx][ny] == '1':
                    heapq.heappush(q, (count, nx, ny))
                else:
                    heapq.heappush(q, (count+1, nx, ny))
                visited[nx][ny] = True


N = int(input())
maze = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dijkstra(0, 0))
