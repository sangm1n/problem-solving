"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 영역 구하기
description : DFS
"""


import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global size
    visited[x][y] = True
    size += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and box[nx][ny] == 0:
            dfs(nx, ny)


M, N, K = map(int, input().split())
box = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
coord = [list(map(int, input().split())) for _ in range(K)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for lx, ly, rx, ry in coord:
    start = (M-ly-1, lx)

    for i in range(ry-ly):
        for j in range(rx-lx):
            box[start[0]-i][start[1]+j] = 1

count = 0
result = []
for i in range(M):
    for j in range(N):
        if box[i][j] == 0 and not visited[i][j]:
            size = 0
            dfs(i, j)
            count += 1
            result.append(size)

print(count)
print(*sorted(result))
