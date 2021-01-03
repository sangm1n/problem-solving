"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 검문
description : 유클리드 호제법
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


M = int(input())
arr = [int(input()) for _ in range(M)]
arr.sort(reverse=True)

tmp = []
for i in range(1, len(arr)):
    tmp.append(arr[i-1] - arr[i])

if len(tmp) == 1:
    result = tmp[0]
elif len(tmp) == 2:
    result = gcd(tmp[0], tmp[1])
else:
    result = tmp[0]
    for i in range(1, len(tmp)):
        result = gcd(result, tmp[i])

for i in range(2, result+1):
    if result % i == 0:
        print(i, end=' ')
        