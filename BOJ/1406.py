"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 에디터
description : Queue
"""

import sys
from collections import deque
input = sys.stdin.readline

string = list(input().rstrip())
N = int(input())
fq = deque(string)
bq = deque()

for _ in range(N):
    edit = input().rstrip()

    if len(edit) > 1:
        fq.append(edit[-1])
    else:
        if fq and edit == 'L':
            bq.appendleft(fq.pop())
        elif bq and edit == 'D':
            fq.append(bq.popleft())
        elif fq and edit == 'B':
            fq.pop()

print("".join(fq + bq))
