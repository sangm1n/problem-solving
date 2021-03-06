"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 거짓말
description : BFS
"""

from collections import deque

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
graph = [list(map(int, input().split()))[1:] for _ in range(M)]

people = [False] * (N+1)
party = [False] * M
for t in truth:
    q = deque()
    q.append(t)
    people[t] = True

    while q:
        v = q.popleft()

        for i in range(len(graph)):
            if v in graph[i]:
                for t in graph[i]:
                    if not people[t]:
                        q.append(t)
                        people[t] = True
                    party[i] = True

print(party.count(False))
