"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


N = int(input())
result = factorial(N)
count, idx = 0, 10

while result % idx == 0:
    count += 1
    idx *= 10

print(count)
