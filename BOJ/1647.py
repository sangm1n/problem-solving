"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 도시 분할 계획
description : MST
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
parent = [x for x in range(N+1)]
result = []
for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))
