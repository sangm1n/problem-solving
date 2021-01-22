"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Puyo Puyo
description : BFS
"""

from collections import deque


def bfs(i, j, total):
    q = deque()
    q.append((i, j))

    count = 1
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and puyo[x][y] == puyo[nx][ny] and not visited[nx][ny]:
                count += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    if count >= 4:
        total += 1
        for i in range(12):
            for j in range(6):
                if visited[i][j]:
                    puyo[i][j] = '.'

    return total


def rearrange():
    for i in range(10, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.' and puyo[i+1][j] == '.':
                idx = i+1

                while idx < 12:
                    if idx == 11 and puyo[idx][j] == '.':
                        puyo[i][j], puyo[idx][j] = puyo[idx][j], puyo[i][j]
                    elif puyo[idx][j] != '.':
                        puyo[i][j], puyo[idx-1][j] = puyo[idx-1][j], puyo[i][j]
                        break
                    idx += 1


puyo = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
while True:
    total = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                total = bfs(i, j, total)

    if total == 0:
        break
    else:
        result += 1

    rearrange()

print(result)
