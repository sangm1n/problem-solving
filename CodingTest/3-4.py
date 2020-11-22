"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 1이 될 때까지
description : 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
    - N에서 1을 뺀다.
    - N을 K로 나눈다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하시오.
"""

N, K = map(int, input().split())

count = 0
while True:
    if N == 1:
        break

    if N % K == 0:
        N //= K
    else:
        N -= 1
    count += 1

print(count)
