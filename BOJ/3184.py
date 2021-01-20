"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 양
description : DFS
"""

import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    global sheep, wolf

    if x < 0 or x > R-1 or y < 0 or y > C-1 or ground[x][y] == '#' or ground[x][y] == '-':
        return False

    if ground[x][y] != '#':
        if ground[x][y] == 'v':
            wolf += 1
        if ground[x][y] == 'o':
            sheep += 1

        ground[x][y] = '-'

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


R, C = map(int, input().split())
ground = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sheep_cnt, wolf_cnt = 0, 0
for i in range(R):
    for j in range(C):
        sheep, wolf = 0, 0
        if dfs(i, j):
            if sheep > wolf:
                sheep_cnt += sheep
            else:
                wolf_cnt += wolf

print(sheep_cnt, wolf_cnt)
