"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 암호제작
description : Math
"""

P, K = map(int, input().split())


def prime_number(n, check):
    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            for j in range(i*2, n+1, i):
                if check[j]:
                    check[j] = False


check = [True] * (K+1)
check[0] = check[1] = False
prime_number(K, check)

for i in range(2, K):
    if check[i] and P % i == 0:
        print("BAD", i)
        exit()
print("GOOD")
