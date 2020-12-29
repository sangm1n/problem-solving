"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 감시 피하기
description : Brute Force
"""

from itertools import combinations

N = int(input())
grid = [list(map(str, input().split())) for _ in range(N)]

tmp = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'X':
            tmp.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y, idx):
    global flag

    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1 or grid[nx][ny] == 'O':
            return

        if grid[nx][ny] == 'S':
            flag = False
            return

        x, y = nx, ny


combination = list(combinations(tmp, 3))
for comb in combination:
    for i, j in comb:
        grid[i][j] = 'O'

    flag = True
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'T':
                for k in range(4):
                    search(i, j, k)

    if flag:
        print("YES")
        exit()

    for i, j in comb:
        grid[i][j] = 'X'

print("NO")
