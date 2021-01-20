"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 물통
description : BFS
"""

from collections import deque

A, B, C = map(int, input().split())
visited = [[False] * 201 for _ in range(201)]


def calc(a, b):
    global q

    if not visited[a][b]:
        visited[a][b] = True
        q.append((a, b))


result = []
q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    z = C - x - y

    if x == 0:
        result.append(z)

    # A -> B
    if x > 0 and y < B:
        val = min(x, B-y)
        calc(x-val, y+val)

    # B -> A
    if y > 0 and x < A:
        val = min(y, A-x)
        calc(x+val, y-val)

    # B -> C
    if y > 0 and z < C:
        val = min(y, C-z)
        calc(x, y-val)

    # C -> B
    if z > 0 and y < B:
        val = min(z, B-y)
        calc(x, y+val)

    # A -> C
    if x > 0 and z < C:
        val = min(x, C-z)
        calc(x-val, y)

    # C -> A
    if z > 0 and x < A:
        val = min(z, A-x)
        calc(x+val, y)

result.sort()
print(*result)
