"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 합이 0인 네 정수
description : Binary Search
"""

from collections import defaultdict

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = defaultdict(int)
for a in A:
    for b in B:
        AB[a+b] += 1

result = 0
for c in C:
    for d in D:
        if -(c+d) in AB:
            result += AB[-(c+d)]

print(result)
