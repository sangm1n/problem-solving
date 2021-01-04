"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 회사에 있는 사람
description : Dictionary
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    name, inout = map(str, input().split())
    if inout == 'leave':
        dic[name] -= 1
    else:
        dic[name] += 1

result = []
for key, value in dic.items():
    if value != 0:
        result.append(key)

result.sort(reverse=True)
for r in result:
    print(r)
