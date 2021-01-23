"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 단지번호붙이기
description : DFS
"""


def dfs(x, y):
    global tmp

    visited[x][y] = True
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            tmp += 1
            dfs(nx, ny)


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
count = []
for i in range(N):
    for j in range(N):
        tmp = 1
        if graph[i][j] == 1:
            dfs(i, j)
            result += 1
            count.append(tmp)

print(result)
count.sort()
[print(c) for c in count]
