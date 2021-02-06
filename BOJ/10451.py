"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 순열 사이클
description : BFS
"""

from collections import deque


def bfs(x):
    q = deque()
    q.append(arr[x])
    visited[arr[x]] = True

    while q:
        v = q.popleft()

        if not visited[arr[v]]:
            visited[arr[v]] = True
            q.append(arr[v])


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = [0] + arr
    visited = [False] * (N+1)

    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)
