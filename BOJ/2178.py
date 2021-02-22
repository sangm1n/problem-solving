"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 미로 탐색
description : BFS
"""

from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])
