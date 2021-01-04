"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 스택
description : Stack
"""

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    instruct = list(input().split())

    if len(instruct) == 2:
        stack.append(int(instruct[1]))
    else:
        if instruct[0] == 'top':
            if not stack:
                print(-1)
            else:
                print(stack[-1])
        elif instruct[0] == 'size':
            print(len(stack))
        elif instruct[0] == 'pop':
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif instruct[0] == 'empty':
            if not stack:
                print(1)
            else:
                print(0)
