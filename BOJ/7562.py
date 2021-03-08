"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 나이트의 이동
description : BFS
"""


from collections import deque


def bfs(i, j, count):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    q = deque()
    q.append((i, j, count))
    visited[i][j] = True

    while q:
        x, y, cnt = q.popleft()
        if x == goal_x and y == goal_y:
            return cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True


T = int(input())
for _ in range(T):
    N = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    visited = [[False for _ in range(N)] for _ in range(N)]
    print(bfs(now_x, now_y, 0))
