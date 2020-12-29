"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연구소
description : DFS
"""

import copy
from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

tmp = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            tmp.append((i, j))


def spread(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1 or lab[nx][ny] == 1:
            continue

        if lab[nx][ny] == 0:
            lab[nx][ny] = 2
            spread(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

combination = combinations(tmp, 3)
result = 0
for comb in combination:
    lab = copy.deepcopy(grid)
    for i in range(3):
        x, y = comb[i][0], comb[i][1]
        lab[x][y] = 1

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                spread(i, j)

    count = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                count += 1
    result = max(result, count)

print(result)
