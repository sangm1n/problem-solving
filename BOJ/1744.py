"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수 묶기
description : Sorting
"""

import sys
input = sys.stdin.readline

N = int(input())

pos, neg, etc = [], [], []
for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        etc.append(num)

pos.sort(reverse=True)
neg.sort()
result = 0

for i in range(1, len(pos), 2):
    result += pos[i-1] * pos[i]
if len(pos) % 2 == 1:
    result += pos[-1]

for i in range(1, len(neg), 2):
    result += neg[i-1] * neg[i]
if len(neg) % 2 == 1:
    if 0 not in etc:
        result += neg[-1]

result += sum(etc)
print(result)
