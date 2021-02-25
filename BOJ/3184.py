"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 양
description : DFS
"""


def dfs(i, j, graph):
    stack = []
    stack.append((i, j))
    sheep, wolf = 0, 0
    if graph[i][j] == 'o':
        sheep += 1
    elif graph[i][j] == 'v':
        wolf += 1
    graph[i][j] = '#'

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#':
                stack.append((nx, ny))
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                graph[nx][ny] = '#'
    return sheep, wolf


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            o, v = dfs(i, j, graph)
            if o > v:
                sheep += o
            else:
                wolf += v

print(sheep, wolf)
