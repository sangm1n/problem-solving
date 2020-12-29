"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 특정 거리의 도시 찾기
description : BFS
"""

from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

tmp = [-1] * (N+1)
tmp[X] = 0


def bfs(start, tmp):
    q = deque([start])

    while q:
        v = q.popleft()
        for i in graph[v]:
            if tmp[i] == -1:
                q.append(i)
                tmp[i] = tmp[v] + 1


bfs(X, tmp)

flag = False
for idx, val in enumerate(tmp):
    if val == K:
        flag = True
        print(idx)

if not flag:
    print(-1)
