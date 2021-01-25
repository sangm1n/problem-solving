"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 섬의 개수
description : DFS
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, visited):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny, visited)


dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        exit()

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited)
                count += 1

    print(count)
