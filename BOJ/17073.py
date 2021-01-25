"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 나무 위의 빗물
description : DFS
"""

import sys
input = sys.stdin.readline


def dfs(visited, n, w):
    stack = [n]
    visited[n] = True

    while stack:
        start = stack.pop()
        water = w[start]

        count = 0
        for v in graph[start]:
            if not visited[v]:
                count += 1

        if count == 0:
            continue

        val = water / count
        w[start] = 0

        for v in graph[start]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                w[v] += val


N, W = map(int, input().split())
graph = [[] for _ in range(N+1)]
water = [0]

for i in range(1, N+1):
    if i == 1:
        water.append(W)
    else:
        water.append(0)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
dfs(visited, 1, water)

result, count = 0, 0
for w in water:
    if w != 0:
        result += w
        count += 1

print(round(result / count, 10))
