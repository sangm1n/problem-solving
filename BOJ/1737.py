"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Pibonacci
description : Dynamic Programming
"""

import math
import sys
sys.setrecursionlimit(10**6)


def pibonacci(num):
    if 0 <= num <= math.pi:
        return 1

    if num in dp:
        return dp[num]

    dp[num] = pibonacci(num - 1) + pibonacci(num - math.pi)
    return dp[num] % 1000000000000000000


N = int(input())

dp = dict()
print(pibonacci(N))
