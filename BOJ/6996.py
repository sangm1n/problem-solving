"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 애너그램
description : Sorting
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = input().split()

    adic = defaultdict(int)
    bdic = defaultdict(int)

    for char in a:
        adic[char] += 1

    for char in b:
        bdic[char] += 1

    if adic == bdic:
        print('{} & {} are anagrams.'.format(a, b))
    else:
        print('{} & {} are NOT anagrams.'.format(a, b))
