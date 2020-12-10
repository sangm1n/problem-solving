"""
자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.
"""

import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [x for x in range(N)]
result = list(combinations(arr, K))
print(len(result))
