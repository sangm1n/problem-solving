"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 탈출
description : BFS
"""

from collections import deque


def spread(water):
    len_w = len(water)

    while len_w:
        x, y = water.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                water.append((nx, ny))

        len_w -= 1


def move(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        len_q = len(q)

        while len_q:
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    elif graph[nx][ny] == 'D':
                        print(visited[x][y])
                        return
            len_q -= 1
        spread(water)

    print("KAKTUS")
    return


R, C = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

water = deque()
hog_x, hog_y = 0, 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            hog_x, hog_y = i, j
            graph[i][j] = '.'
        if graph[i][j] == '*':
            water.append((i, j))

spread(water)
move(hog_x, hog_y)
