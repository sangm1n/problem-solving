"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연구소 2
description : BFS
"""

from itertools import combinations
from collections import deque
import copy


def spread(q):
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and tmp[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, count + 1))


def check(visited, tmp):
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and tmp[i][j] == 1:
                continue

            if visited[i][j] == 0:
                count += 1

    return count == M


def spread_time(visited):
    count = 0
    for v in visited:
        count = max(count, max(v))

    return count


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
            lab[i][j] = 0

combination = list(combinations(virus, M))
answer = int(1e9)
for comb in combination:
    tmp = copy.deepcopy(lab)

    for c in comb:
        tmp[c[0]][c[1]] = 2

    visited = [[0] * N for _ in range(N)]
    virus = deque()
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 2:
                virus.append((i, j, 0))

    spread(virus)
    status = check(visited, tmp)
    time = spread_time(visited)

    if status:
        answer = min(answer, time)

print(-1 if answer == int(1e9) else answer)
