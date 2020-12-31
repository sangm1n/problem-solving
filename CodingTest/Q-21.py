"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 인구 이동
description : BFS
"""

from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, index):
    q = deque([(x, y)])
    base = [(x, y)]
    tmp[x][y] = index
    count = 1
    total = country[x][y]

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < N and 0 <= ny < N and tmp[nx][ny] == 0 and \
                    L <= abs(country[px][py] - country[nx][ny]) <= R:
                tmp[nx][ny] = index
                q.append((nx, ny))
                base.append((nx, ny))
                total += country[nx][ny]
                count += 1

    for i, j in base:
        country[i][j] = total // count


result = 0
while True:
    tmp = [[0] * N for _ in range(N)]

    index = 1
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 0:
                bfs(i, j, index)
                index += 1

    if index == N**2 + 1:
        print(result)
        break

    result += 1
