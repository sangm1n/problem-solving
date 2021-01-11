"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : N과 M (7)
description : Permutation
"""

from itertools import product

N, M = map(int, input().split())
arr = list(map(int, input().split()))

perm = list(product(arr, repeat=M))
perm.sort()
[print(*p) for p in perm]
