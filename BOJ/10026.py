"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 적록색약
description : BFS
"""

from collections import deque

N = int(input())
eyes = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited_sick = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def normal(i, j):
    q = deque([[i, j]])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and eyes[x][y] == eyes[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])


def sick(i, j):
    q = deque([[i, j]])
    visited_sick[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited_sick[nx][ny] == 0:
                if eyes[x][y] == 'B' and eyes[nx][ny] == 'B':
                    visited_sick[nx][ny] = 1
                    q.append([nx, ny])
                elif eyes[x][y] in ['R', 'G'] and eyes[nx][ny] in ['R', 'G']:
                    visited_sick[nx][ny] = 1
                    q.append([nx, ny])


count, count_sick = 0, 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            normal(i, j)
            count += 1
        if visited_sick[i][j] == 0:
            sick(i, j)
            count_sick += 1

print(count, count_sick)
