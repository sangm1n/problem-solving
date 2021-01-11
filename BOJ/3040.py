"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 백설 공주와 일곱 난쟁이
description : Brute Force
"""

import sys
from itertools import combinations
input = sys.stdin.readline

hats = [int(input()) for _ in range(9)]

combination = list(combinations(hats, 7))
for comb in combination:
    if sum(comb) == 100:
        for num in comb:
            print(num)
        break
