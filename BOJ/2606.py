"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 바이러스
description : DFS
"""


def dfs(n):
    global count
    visited[n] = True
    count += 1

    for v in network[n]:
        if not visited[v]:
            visited[v] = True
            dfs(v)


N = int(input())
M = int(input())
network = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

count = 0
dfs(1)
print(count - 1)
