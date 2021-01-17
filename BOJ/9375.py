"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 패션왕 신해빈
description : Math
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dic = defaultdict(list)
    for _ in range(N):
        name, category = map(str, input().split())
        dic[category].append(name)

    result = 1
    for value in dic.values():
        result *= len(value) + 1

    print(result - 1)

