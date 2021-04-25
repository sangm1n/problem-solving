"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 도시 분할 계획
description : Kruskal Algorithm
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


N, M = map(int, input().split())
graph = []
for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

parent = [x for x in range(N+1)]
graph.sort()

result, max_cost = 0, 0

for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)
