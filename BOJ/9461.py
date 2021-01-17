"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 파도반 수열
description : Dynamic Programming
"""

P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    P.append(P[i-1] + P[i-5])

T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N])
