"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 인구 이동
description : Brute Force
"""

from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global total, count

    q = deque()
    q.append((x, y))
    united[x][y] = 1

    flag = True
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue

            if L <= abs(country[a][b] - country[nx][ny]) <= R:
                total += country[nx][ny]
                count += 1
                united[nx][ny] = 1
                q.append((nx, ny))
            else:
                flag = False
                break
        if not flag:
            break


for _ in range(10):
    united = [[0] * N for _ in range(N)]
    a, b = [], []
    for i in range(N):
        for j in range(N):
            total, count = 0, 0
            bfs(i, j)
            a.append(total)
            b.append(count)

    print(united)
    print(a, b)


