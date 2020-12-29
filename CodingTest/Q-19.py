"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 연산자 끼워 넣기
description : Brute Force
"""

from itertools import permutations

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
exp = list(map(int, input().split()))

tmp = ['+', '-', '*', '/']
base = []
for i in range(len(exp)):
    for j in range(exp[i]):
        base.append(tmp[i])

permutation = set(list(permutations(base, N-1)))

maximum, minimum = -10e9, 10e9
for perm in permutation:
    result = arr[0]
    for i in range(len(perm)):
        if perm[i] == '+':
            result += arr[i+1]
        elif perm[i] == '-':
            result -= arr[i+1]
        elif perm[i] == '*':
            result *= arr[i+1]
        else:
            if result < 0 and arr[i+1] > 0:
                result = -(-result // arr[i+1])
            else:
                result //= arr[i+1]

    maximum = max(maximum, result)
    minimum = min(minimum, result)

print(maximum)
print(minimum)
