"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for i in range(N):
   dic[int(input())] += 1

dic = sorted(dic.items())
for i in range(len(dic)):
    for j in range(dic[i][1]):
        print(dic[i][0])
