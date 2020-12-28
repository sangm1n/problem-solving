"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 토마토
description : BFS
"""

from collections import deque


def bfs():
    result = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))
                result = max(result, box[nx][ny] - 1)

    return result


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

count = bfs()

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()
print(count)
