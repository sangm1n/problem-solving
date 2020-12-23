"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 볼링공 고르기
description : A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주합니다.
볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.

N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.
"""

from itertools import combinations

N, M = map(int, input().split())
ball = list(map(int, input().split()))

comb = list(combinations(ball, 2))
count = 0
for com in comb:
    if com[0] == com[1]:
        continue
    count += 1

print(count)
