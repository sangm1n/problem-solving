"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 알파벳
description : DFS
"""

import sys
input = sys.stdin.readline


def dfs(x, y, count):
    global result

    result = max(result, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in alphabet:
            alphabet.add(graph[nx][ny])
            dfs(nx, ny, count + 1)
            alphabet.remove(graph[nx][ny])


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alphabet = set(graph[0][0])
result = 0
dfs(0, 0, 1)

print(result)
