"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 큐
description : Queue
"""

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())

for _ in range(N):
    instruct = list(input().split())

    if len(instruct) == 2:
        q.append(int(instruct[1]))
    else:
        if instruct[0] == 'front':
            print(-1 if not q else q[0])
        elif instruct[0] == 'back':
            print(-1 if not q else q[-1])
        elif instruct[0] == 'size':
            print(len(q))
        elif instruct[0] == 'empty':
            print(1 if not q else 0)
        elif instruct[0] == 'pop':
            print(-1 if not q else q.popleft())
