"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 유기농 배추
description : DFS
"""

import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    visited[x][y] = True
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
