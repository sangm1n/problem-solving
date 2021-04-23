"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 경쟁적 전염
description : BFS
"""

from collections import deque


def spread(q, arr, S):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        virus, x, y, time = q.popleft()

        if time == S:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(arr) and 0 <= ny < len(arr) and arr[nx][ny] == 0:
                arr[nx][ny] = virus
                q.append((arr[nx][ny], nx, ny, time + 1))


N, K = map(int, input().split())
cylinder = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

tmp = []
for i in range(N):
    for j in range(N):
        if cylinder[i][j] != 0:
            tmp.append((cylinder[i][j], i, j, 0))

tmp.sort()
q = deque(tmp)

spread(q, cylinder, S)
print(cylinder[X-1][Y-1])
