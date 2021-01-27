"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 구슬 탈출
description : BFS
"""

from collections import deque


def bfs(q, visited):
    while q:
        rx, ry, bx, by, count = q.popleft()

        if count > 10:
            break

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])

            if marble[nbx][nby] == 'O':
                continue

            if marble[nrx][nry] == 'O':
                return 1

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, count + 1))

    return 0


def move(x, y, dx, dy):
    count = 0
    while True:
        if marble[x + dx][y + dy] == '#' or marble[x][y] == 'O':
            break

        x += dx
        y += dy
        count += 1

    return x, y, count


N, M = map(int, input().split())
marble = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if marble[i][j] == 'R':
            rx, ry = i, j
        if marble[i][j] == 'B':
            bx, by = i, j

q = deque()
q.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True
result = bfs(q, visited)

print(result)
