"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 벽 부수고 이동하기
description : BFS
"""

from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j, 1))
    visited[1][i][j] = 1

    while q:
        x, y, wall = q.popleft()

        if x == N-1 and y == M-1:
            return visited[wall][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[wall][nx][ny]:
                if graph[nx][ny] == 0:
                    visited[wall][nx][ny] = visited[wall][x][y] + 1
                    q.append((nx, ny, wall))
                if graph[nx][ny] == 1 and wall == 1:
                    visited[0][nx][ny] = visited[wall][x][y] + 1
                    q.append((nx, ny, wall - 1))

    return -1


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
