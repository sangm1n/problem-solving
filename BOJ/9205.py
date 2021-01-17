"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 맥주 마시면서 걸어가기
description : BFS
"""

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(N)]
    festival = list(map(int, input().split()))
    conv.append(festival)

    visited = [False] * (N + 2)
    q = deque([home])
    visited[0] = True

    flag = False
    while q:
        x, y = q.popleft()

        if x == festival[0] and y == festival[1]:
            flag = True

        for i in range(len(conv)):
            nx, ny = conv[i][0], conv[i][1]

            if abs(nx-x) + abs(ny-y) <= 1000 and not visited[i+1]:
                visited[i+1] = True
                q.append([nx, ny])

    print("happy" if flag else "sad")
