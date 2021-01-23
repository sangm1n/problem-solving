"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숨바꼭질
description : BFS
"""

from collections import deque


def bfs(start, end):
    q = deque()
    q.append((start, 0))

    while q:
        val, time = q.popleft()

        if val == end:
            return time

        for x in [val-1, val+1, val*2]:
            if 0 <= x < len(visited) and not visited[x]:
                q.append((x, time+1))
                visited[x] = True


N, K = map(int, input().split())
visited = [False] * 100001

result = bfs(N, K)
print(result)
