"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 행성 터널
description : Graph
"""

import sys
input = sys.stdin.readline

N = int(input())
planet = [list(map(int, input().split())) for _ in range(N)]
parent = [x for x in range(N+1)]

x, y, z = [], [], []
for i in range(N):
    x.append((planet[i][0], i+1))
    y.append((planet[i][1], i+1))
    z.append((planet[i][2], i+1))

x.sort()
y.sort()
z.sort()


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
edges.sort()

result = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
