"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : DSLR
description : Graph
"""

from collections import deque
import sys
input = sys.stdin.readline


def bfs(visited, base, answer):
    first = [base, ""]

    q = deque([first])
    visited[base] = True

    while q:
        x, y = q.popleft()

        if x == answer:
            return y

        val = (x * 2) % 10000
        if not visited[val]:
            visited[val] = True
            q.append([val, y + 'D'])

        val = (x - 1) % 10000
        if not visited[val]:
            visited[val] = True
            q.append([val, y + "S"])

        val = (x % 1000 * 10) + (x // 1000)
        if not visited[val]:
            visited[val] = True
            q.append([val, y + "L"])

        val = (x % 10 * 1000) + (x // 10)
        if not visited[val]:
            visited[val] = True
            q.append([val, y + "R"])


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000

    result = bfs(visited, A, B)
    print(result)
