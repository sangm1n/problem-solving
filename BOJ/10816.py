"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""

import sys
from collections import Counter

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
num_count = Counter(number)

M = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

for idx in compare:
    print(num_count[idx], end=' ')
