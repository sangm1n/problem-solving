"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 이중 우선순위 큐
description : binary tree
"""

import sys
import bisect
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    result = deque()
    tmp = dict()
    for _ in range(N):
        alpha, digit = map(str, input().split())
        digit = int(digit)

        if alpha == 'I':
            try:
                tmp[digit] += 1
            except:
                tmp[digit] = 1
                bisect.insort_left(result, digit)
        else:
            if not result:
                continue

            if digit == 1:
                max_val = result[-1]
                if tmp[max_val] == 1:
                    tmp.pop(max_val)
                    result.pop()
                else:
                    tmp[max_val] -= 1
            else:
                min_val = result[0]
                if tmp[min_val] == 1:
                    tmp.pop(min_val)
                    result.popleft()
                else:
                    tmp[min_val] -= 1

    if not result:
        print('EMPTY')
    else:
        print(result[-1], result[0], end=' ')
