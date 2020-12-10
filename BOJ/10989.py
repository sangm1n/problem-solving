"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline())

arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        continue

    for _ in range(arr[i]):
        print(i)
