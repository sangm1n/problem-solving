"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 탑
description : Stack
"""

import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

stack, result = [], []
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()

    if not stack:
        result.append(0)
    stack.append((i+1, tower[i]))

print(*result)
