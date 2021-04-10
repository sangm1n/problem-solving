"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 소수 찾기
description : Brute Force
"""

from itertools import permutations


def prime_number():
    arr = [True] * 10000000
    arr[0], arr[1] = False, False

    for i in range(2, int(10000000 ** 0.5) + 1):
        if arr[i]:
            for j in range(2 * i, 10000000, i):
                arr[j] = False

    return arr


def solution(numbers):
    prime_arr = prime_number()

    result = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            value = int("".join(perm))
            if prime_arr[value]:
                result.add(value)

    return len(result)


if __name__ == '__main__':
    number = "011"

    result = solution(number)
    print(result)
