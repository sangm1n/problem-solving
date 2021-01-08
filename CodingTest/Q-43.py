"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 어두운 길
description : Graph
"""

N, M = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(M)]
parent = [x for x in range(N+1)]


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


load.sort(key=lambda x: x[2])
total, result = 0, 0
for i in range(M):
    a, b, cost = load[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
    total += cost

print(total-result)
