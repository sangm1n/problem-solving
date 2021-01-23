"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 미로 탐색
description : BFS
"""

from collections import deque


def bfs(i, j, count):
    q = deque()
    q.append((i, j, count))
    graph[i][j] = count
    visited[i][j] = True

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0, 1)

print(graph[N-1][M-1])
