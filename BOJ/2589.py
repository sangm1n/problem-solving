"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 보물섬
description : BFS
"""

from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))

    visited = [[0] * W for _ in range(L)]
    visited[i][j] = 1
    result = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < W and visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                result = max(result, visited[nx][ny])
                q.append((nx, ny))

    return result - 1


L, W = map(int, input().split())
graph = [list(input()) for _ in range(L)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = []
answer = 0
for i in range(L):
    for j in range(W):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
