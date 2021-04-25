"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 팀 결성
description : Disjoint set
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
operation = [list(map(int, input().split())) for _ in range(M)]
parent = [x for x in range(N+1)]

for opt, a, b in operation:
    if opt == 0:
        union_parent(parent, a, b)
    else:
        print("YES" if find_parent(parent, a) == find_parent(parent, b) else "NO")
