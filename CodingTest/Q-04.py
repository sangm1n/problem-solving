"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 만들 수 없는 금액
description : 동네 편의점 주인은 N개의 동전을 가지고 있습니다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
예를 들어, N=5이고, 각 동전이 3원, 2원, 1원, 1원, 9원짜리 동전이라고 가정합시다.
이때 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.
"""

from itertools import combinations

N = int(input())
coin = list(map(int, input().split()))

tmp = [False for _ in range(sum(coin) + 1)]
tmp[0] = True

for i in range(1, N+1):
    if i == 1:
        for j in coin:
            tmp[j] = True
        continue

    comb = list(combinations(coin, i))
    for j in comb:
        total = sum(j)
        if tmp[total]:
            continue
        tmp[total] = True

print(tmp.index(False))
