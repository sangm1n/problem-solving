"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 두 배열의 원소 교체
description : 두 배열 A와 B는 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 서로 바꾸는 것을 말한다.
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하라.
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    min_A, max_B = min(A), max(B)
    A[A.index(min_A)], B[B.index(max_B)] = B[B.index(max_B)], A[A.index(min_A)]

print(sum(A))
