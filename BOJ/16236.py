"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 아기 상어
description : Implementation
"""

from collections import deque
import heapq

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def search(i, j, count, size):
    space[i][j] = 0
    q = deque([[i, j, count]])
    dist = []

    visited = set()
    while q:
        x, y, count = q.popleft()
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))

                if space[nx][ny] == 0 or space[nx][ny] == size:
                    q.append([nx, ny, count+1])
                    continue

                if space[nx][ny] <= size:
                    heapq.heappush(dist, (count+1, nx, ny))

    if dist:
        return dist[0]
    else:
        return None


result = 0
size, eat = 2, 0
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            while True:
                next_val = search(i, j, 0, size)

                if not next_val:
                    break

                count, nx, ny = next_val
                result += count

                eat += 1
                if eat == size:
                    size += 1
                    eat = 0

                i, j = nx, ny

print(result)
