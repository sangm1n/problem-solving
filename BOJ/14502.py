"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연구소
description : BFS
"""

from itertools import combinations
from collections import deque
import copy


def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] != 1 and not visited[nx][ny]:
                q.append((nx, ny))
                tmp[nx][ny] = 2
                visited[nx][ny] = True


def count_safe():
    count = 0
    for t in tmp:
        count += t.count(0)

    return count


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

block = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            block.append((i, j))

comb = list(combinations(block, 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for a, b, c in comb:
    tmp = copy.deepcopy(graph)
    tmp[a[0]][a[1]] = 1
    tmp[b[0]][b[1]] = 1
    tmp[c[0]][c[1]] = 1

    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                bfs(i, j, visited)
    result = max(result, count_safe())

print(result)
