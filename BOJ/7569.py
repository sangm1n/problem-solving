"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 토마토
description : BFS
"""

from collections import deque


def bfs(q):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    count = 0
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and boxes[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                count = max(count, boxes[nz][nx][ny] - 1)

    return count


M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))

result = bfs(q)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                print(-1)
                exit()
print(result)
