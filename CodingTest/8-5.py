"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 1로 만들기
description : 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
    - X가 5로 나누어 떨어지면, 5로 나눈다.
    - X가 3으로 나누어 떨어지면, 3으로 나눈다.
    - X가 2로 나누어 떨어지면, 2로 나눈다.
    - X에서 1을 뺀다.
정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[N])
