"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자 고르기
description : BFS
"""

N = int(input())
first = [x for x in range(1, N+1)]
second = [int(input()) for _ in range(N)]

arr = list(zip(first, second))
tmp = arr.copy()
result = set()

while arr:
    a, b = arr.pop()

    if (b, a) in tmp:
        result.add(a)
        result.add(b)

print(len(result))
result = sorted(list(result))
[print(x) for x in result]
