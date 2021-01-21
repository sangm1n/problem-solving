"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 나무 탈출
description : DFS
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n, count, visited):
    global result

    visited[n] = True

    for i in tree[n]:
        if not visited[i]:
            dfs(i, count + 1, visited)

    if n != 1 and len(tree[n]) == 1:
        result += count


N = int(input())
tree = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = 0
visited = [False] * (N+1)
dfs(1, 0, visited)

print("No" if result % 2 == 0 else "Yes")
