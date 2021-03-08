"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 단지번호붙이기
description : DFS
"""


def dfs(x, y, visited):
    global count
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            count += 1
            dfs(nx, ny, visited)


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
total = []
for i in range(N):
    for j in range(N):
        count = 1
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, visited)
            result += 1
            total.append(count)

print(result)
total.sort()
[print(x) for x in total]
