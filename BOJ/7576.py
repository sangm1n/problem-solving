"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 토마토
description : BFS
"""

from collections import deque


def bfs():
    global q

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

result = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit()
    result = max(result, max(g))
print(result - 1)
