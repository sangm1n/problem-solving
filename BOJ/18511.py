"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 큰 수 구성하기
description : Brute Force
"""

from itertools import product

N, K = map(int, input().split())
arr = list(map(int, input().split()))

length = len(str(N))
flag = True
while length > 0:
    prod = list(product(arr, repeat=length))
    prod.sort(reverse=True)

    for p in prod:
        value = int("".join(map(str, p)))
        if value <= N:
            print(value)
            flag = False
            break

    if not flag:
        break

    length -= 1
