"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 탑승구
description : Graph
"""

G = int(input())
P = int(input())
docking = [int(input()) for _ in range(P)]
parent = [0] * (G+1)
for i in range(G+1):
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


count = 0
for i in range(P):
    tmp = find_parent(parent, docking[i])
    if tmp == 0:
        break
    union_parent(parent, tmp, tmp - 1)
    count += 1

print(count)
