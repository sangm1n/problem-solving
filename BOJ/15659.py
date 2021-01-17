"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연산자 끼워넣기 (3)
description : Back Tracking
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque(map(int, input().split()))
sign = list(map(int, input().split()))


def bfs(idx, sign):
    global result

    start = [idx, arr[idx], "", sign]
    q = deque([start])

    while q:
        idx, num, tot, s = q.popleft()

        if idx < N and s[0] > 0:
            sc = s.copy()
            sc[0] -= 1
            q.append([idx+1, arr[idx+1], tot + str(num) + "+", sc])

        if idx < N and s[1] > 0:
            sc = s.copy()
            sc[1] -= 1
            q.append([idx+1, arr[idx+1], tot + str(num) + "-", sc])

        if idx < N and s[2] > 0:
            sc = s.copy()
            sc[2] -= 1
            q.append([idx+1, arr[idx+1], tot + str(num) + "*", sc])

        if idx < N and s[3] > 0:
            sc = s.copy()
            sc[3] -= 1
            q.append([idx+1, arr[idx+1], tot + str(num) + "//", sc])

        if sum(s) == 0:
            result.append(eval(tot + str(arr[-1])))


result = []
bfs(0, sign)
print(max(result))
print(min(result))
