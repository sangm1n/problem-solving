"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 절댓값 힙
description : Priority Queue
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    x = int(input())

    if x != 0:
        if x > 0:
            heapq.heappush(q, (x, "plus"))
        else:
            heapq.heappush(q, (-x, "minus"))
    else:
        if not q:
            print(0)
        else:
            value, status = heapq.heappop(q)

            print(value if status == "plus" else -value)



