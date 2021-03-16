"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 알파벳
description : DFS
"""


def dfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and alphabet[graph[nx][ny]] == 0:
            alphabet[graph[nx][ny]] = 1
            dfs(nx, ny, count + 1)
            alphabet[graph[nx][ny]] = 0


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        graph[i][j] = ord(graph[i][j]) - 65
alphabet = [0 for _ in range(26)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 1
alphabet[graph[0][0]] = 1
dfs(0, 0, result)
print(result)
