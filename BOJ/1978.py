"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

import sys


def find_prime(number):
    prime_num = [True] * (number + 1)
    prime_num[0], prime_num[1] = False, False

    result = []
    for i in range(2, number+1):
        for j in range(2*i, number+1, i):
            if prime_num[i]:
                prime_num[j] = False
            else:
                continue

    for idx, cond in enumerate(prime_num):
        if cond:
            result.append(idx)

    return result


N = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

compare = find_prime(1000)
count = 0
for cond in check:
    if cond in compare:
        count += 1

print(count)
