"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 안전 영역
description : DFS
"""

import copy
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y, visited, tmp, height):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and tmp[nx][ny] > height:
            dfs(nx, ny, visited, tmp, height)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_height = 0
for g in graph:
    max_height = max(max_height, max(g))

max_area = 0
for height in range(max_height+1):
    tmp = copy.deepcopy(graph)
    visited = [[False] * N for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(N):
            if tmp[i][j] > height and not visited[i][j]:
                dfs(i, j, visited, tmp, height)
                count += 1

    max_area = max(max_area, count)

print(max_area)
