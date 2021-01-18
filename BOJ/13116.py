"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 30번
description : Tree
"""

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    while True:
        if A == B:
            print(10 * A)
            break

        if A < B:
            B //= 2
        else:
            A //= 2
