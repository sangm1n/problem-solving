"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 집합
description : Set
"""

import sys
input = sys.stdin.readline

M = int(input())

S = set()
for _ in range(M):
    instruct = list(map(str, input().split()))

    if instruct[0] == 'add':
        S.add(int(instruct[1]))
    elif instruct[0] == 'remove':
        if int(instruct[1]) in S:
            S.remove(int(instruct[1]))
        else:
            continue
    elif instruct[0] == 'check':
        print(1 if int(instruct[1]) in S else 0)
    elif instruct[0] == 'toggle':
        if int(instruct[1]) in S:
            S.remove(int(instruct[1]))
        else:
            S.add(int(instruct[1]))
    elif instruct[0] == 'all':
        S = {x for x in range(1, 21)}
    elif instruct[0] == 'empty':
        S = set()
