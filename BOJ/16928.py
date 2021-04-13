"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 뱀과 사다리 게임
description : BFS
"""

from collections import deque


def start_game(start, visited, grid):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        pos = q.popleft()

        if pos == 100:
            return visited[pos]

        for i in range(1, 7):
            new_pos = pos + i

            if new_pos < 101:
                move = grid[new_pos]

                if not visited[move]:
                    q.append(move)
                    visited[move] = visited[pos] + 1


N, M = map(int, input().split())
visited = [0] * 101
grid = [*range(101)]

for i in range(N + M):
    start, end = map(int, input().split())
    grid[start] = end

result = start_game(1, visited, grid)
print(result - 1)
