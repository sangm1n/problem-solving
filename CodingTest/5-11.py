"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 미로 탈출
description : N X M 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
사용자의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 사용자가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 반드시 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
"""

from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append([i, j])

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1 or maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[i][j] + 1
                queue.append([nx, ny])

    return maze[N-1][M-1]


print(bfs(0, 0))
