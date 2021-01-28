"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 나이트의 이동
description : BFS
"""


from collections import deque


def bfs(i, j, count):
    q = deque()
    q.append((i, j, count))

    while q:
        x, y, cnt = q.popleft()

        if x == end_x and y == end_y:
            return cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True


dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]

T = int(input())
for _ in range(T):
    I = int(input())

    visited = [[False] * I for _ in range(I)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    result = bfs(start_x, start_y, 0)
    print(result)
