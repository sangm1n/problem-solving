"""
유이니가 미로를 탈출하는 법
"""

from collections import deque


def turn_left(next, x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        if dx[i] == x and dy[i] == y:
            return dx[(i+next) % 4], dy[(i+next) % 4]


def turn_right(next, x, y):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        if dx[i] == x and dy[i] == y:
            return dx[(i+next) % 4], dy[(i+next) % 4]


def start(i, j, pos_x, pos_y):
    q = deque()
    q.append((i, j, pos_x, pos_y))
    visited[i][j] = 1

    count = 0
    while q:
        x, y, dir_x, dir_y = q.popleft()

        if x == N-1 and y == N-1:
            return count

        new_x, new_y = turn_left(1, dir_x, dir_y)
        nx, ny = x + new_x, y + new_y
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] < 2 and graph[nx][ny] == 0:
            q.append((nx, ny, new_x, new_y))
            visited[nx][ny] += 1
            count += 1
            continue
        else:
            for i in range(4):
                xx, yy = turn_right(i+1, new_x, new_y)
                nx, ny = x + xx, y + yy

                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] < 2 and graph[nx][ny] == 0:
                    q.append((nx, ny, xx, yy))
                    visited[nx][ny] += 1
                    count += 1
                    break


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

pos_x, pos_y = 0, 0
if graph[0][1] == 0:
    pos_x, pos_y = 0, 1
elif graph[1][0] == 0:
    pos_x, pos_y = 1, 0

result = start(0, 0, pos_x, pos_y)
print(result)
