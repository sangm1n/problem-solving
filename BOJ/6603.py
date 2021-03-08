"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 로또
description : Combination
"""

from itertools import combinations

while True:
    tmp = list(map(int, input().split()))

    if tmp[0] == 0:
        break

    K, lotto = tmp[0], tmp[1:]

    comb = list(combinations(lotto, 6))
    comb.sort(key=lambda x: x)
    [print(*c) for c in comb]
    print()
