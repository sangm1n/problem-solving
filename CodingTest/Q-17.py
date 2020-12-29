"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 경쟁적 전염
description : BFS
"""

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp = []
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            tmp.append((grid[i][j], 0, i, j))

tmp.sort()
q = deque(tmp)


def bfs(q):
    while q:
        virus, time, x, y = q.popleft()
        if time == S:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = virus
                q.append((grid[nx][ny], time + 1, nx, ny))


bfs(q)
print(grid[X-1][Y-1])
