"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 여행 계획
description : Graph
"""

N, M = map(int, input().split())
trip = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(N):
    for j in range(N):
        if trip[i][j] == 1:
            union_parent(parent, i+1, j+1)

for i in range(1, len(plan)):
    if find_parent(parent, plan[i-1]) != find_parent(parent, plan[i]):
        print("NO")
        exit()
print("YES")
