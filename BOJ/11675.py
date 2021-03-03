"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Jumbled Communication
description : 비트 연산
"""

N = int(input())
arr = list(map(int, input().split()))

for a in arr:
    for i in range(100001):
        if int(bin(i ^ (i << 1) & 255), 2) == a:
            print(i, end=' ')
            break
