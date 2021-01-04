"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 최대 힙
description : Heap
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())

    if x == 0:
        if not hq:
            print(0)
        else:
            num = heapq.heappop(hq)
            print(-num)
    else:
        heapq.heappush(hq, -x)
