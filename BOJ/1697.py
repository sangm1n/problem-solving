"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숨바꼭질
description : BFS
"""

from collections import deque


def bfs(i, visited):
    q = deque()
    q.append(i)
    visited[i] = 1

    while q:
        x = q.popleft()

        if x == K:
            return visited[x] - 1

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1


N, K = map(int, input().split())

visited = [0] * 100001

print(bfs(N, visited))
