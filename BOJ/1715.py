"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 카드 정렬하기
description : Sorting
"""

import heapq

N = int(input())
q = []
[heapq.heappush(q, int(input())) for _ in range(N)]

result = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a + b)
    result += a + b

print(result)
