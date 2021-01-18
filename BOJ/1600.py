"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 말이 되고픈 원숭이
description : BFS
"""

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hx = [-2, -2, -1, 1, 2, 2, -1, 1]
hy = [-1, 1, -2, -2, -1, 1, 2, 2]


def bfs(i, j, k):
    q = deque([[i, j, k]])
    while q:
        x, y, z = q.popleft()

        if x == (H-1) and y == (W-1):
            return check[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and check[nx][ny][z] == 0 and grid[nx][ny] == 0:
                check[nx][ny][z] = check[x][y][z] + 1
                q.append([nx, ny, z])

        if z == K:
            continue

        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]

            if 0 <= nx < H and 0 <= ny < W and check[nx][ny][z+1] == 0 and grid[nx][ny] == 0:
                check[nx][ny][z+1] = check[x][y][z] + 1
                q.append([nx, ny, z+1])
    return -1


grid = [list(map(int, input().split())) for _ in range(H)]
check = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

print(bfs(0, 0, 0))
