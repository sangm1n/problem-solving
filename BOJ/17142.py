"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연구소 3
description : BFS
"""

from collections import deque
from itertools import combinations
from copy import deepcopy


def spread_virus(lab, comb, M):
    visited = [[0 for _ in range(len(lab))] for _ in range(len(lab))]
    tmp = deepcopy(lab)

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q = deque()
    for i in range(M):
        x, y, cnt = comb[i][0], comb[i][1], 0
        q.append((x, y, cnt))
        visited[x][y] = 1

    total = 0
    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(lab) and 0 <= ny < len(lab) and not visited[nx][ny] and tmp[nx][ny] != 1:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    total = cnt + 1
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1

    for i in range(len(tmp)):
        if 0 in tmp[i]:
            return -1
    return total


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))

result = int(1e9)
combination = list(combinations(virus, M))
for comb in combination:
    time = spread_virus(lab, comb, M)
    if time != -1:
        result = min(result, time)

print(-1 if result == int(1e9) else result)
