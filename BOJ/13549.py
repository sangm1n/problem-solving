"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숨바꼭질 3
description : BFS
"""

from collections import deque


def bfs(i, visited):
    q = deque()
    q.append(i)
    visited[i] = True

    while q:
        x = q.popleft()

        if x == K:
            return line[x]

        for nx in (x*2, x-1, x+1):
            if 0 <= nx <= 100000 and not visited[nx]:
                if nx == x*2:
                    line[nx] = line[x]
                else:
                    line[nx] = line[x] + 1

                q.append(nx)
                visited[nx] = True


N, K = map(int, input().split())

line = [0] * 100001
visited = [False] * 100001

print(bfs(N, visited))
