"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 골드바흐의 추측
description : 소수 판정
"""

import math
import sys
input = sys.stdin.readline


def prime_number(n):
    tmp = [True] * (n+1)
    tmp[0], tmp[1] = False, False

    for i in range(2, int(math.sqrt(n)) + 1):
        if tmp[i]:
            for j in range(i*2, n + 1, i):
                tmp[j] = False
    tmp[2] = False

    return tmp


prime = prime_number(1000000)
while True:
    N = int(input())

    if N == 0:
        break

    result = 0
    flag = False
    for idx, val in enumerate(prime):
        if val and prime[(N-idx)]:
            result = idx
            flag = True
            break

    if flag:
        print('{} = {} + {}'.format(N, result, N - result))
    else:
        print("Goldbach's conjecture is wrong.")
