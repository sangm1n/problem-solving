"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 구슬 탈출 2
description : BFS
"""

from collections import deque


def move(x, y, dx, dy):
    count = 0
    while marble[x + dx][y + dy] != '#' and marble[x][y] != 'O':
        x += dx
        y += dy
        count += 1

    return x, y, count


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, total = q.popleft()

        if rx == holeX and ry == holeY:
            return total

        if total > 10:
            return -1

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])

            if nrx == holeX and nry == holeY and nbx == holeX and nby == holeY:
                continue

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, total + 1))

    return -1


N, M = map(int, input().split())
marble = [list(input()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

blueX, blueY, redX, redY, holeX, holeY = 0, 0, 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if marble[i][j] == 'B':
            blueX, blueY = i, j
        if marble[i][j] == 'R':
            redX, redY = i, j
        if marble[i][j] == 'O':
            holeX, holeY = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = bfs(redX, redY, blueX, blueY)
print(result)
