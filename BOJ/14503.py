"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 로봇 청소기
description : Simulation
"""


from collections import deque


def turn_left(d):
    return (d - 1) % 4


def go_back(d):
    return (d + 2) % 4


def cleaning(r, c, d, grid):
    global result

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((r, c))
    grid[r][c] = '#'
    result += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            d = turn_left(d)
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = '#'
                q.append((nx, ny))
                result += 1
                break

            if i == 3:
                nd = go_back(d)
                nx, ny = x + dx[nd], y + dy[nd]

                if grid[nx][ny] == 1:
                    return
                q.append((nx, ny))


N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

result = 0
cleaning(r, c, d, grid)
print(result)
