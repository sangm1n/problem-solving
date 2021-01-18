"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 결혼식
description : BFS
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
friends = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False] * (N+1)
visited[1] = True

count = 0
for i in friends[1]:
    if not visited[i]:
        visited[i] = True
        count += 1

    for j in friends[i]:
        if not visited[j]:
            visited[j] = True
            count += 1

print(count)
