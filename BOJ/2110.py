"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자판 점프
description : DFS
"""


def dfs(x, y, tmp):
    global result

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if len(tmp) == 6:
        result.add(tmp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, tmp + str(graph[nx][ny]))


result = set()
graph = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(i, j, str(graph[i][j]))

print(len(result))
