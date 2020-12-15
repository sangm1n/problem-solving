"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 효율적인 화폐 구성
description : N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

dp = [10001] * (M+1)
dp[0] = 0
for i in range(N):
    for j in range(money[i], M+1):
        dp[j] = min(dp[j], dp[j - money[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
