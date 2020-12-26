"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 에라토스테네스의 체
"""

import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j *= 2

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
