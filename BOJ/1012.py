"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 유기농 배추
description : DFS
"""


def dfs(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = []
    stack.append((i, j))
    graph[i][j] = 0

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                stack.append((nx, ny))
                graph[nx][ny] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
