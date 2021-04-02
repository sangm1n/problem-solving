"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : N으로 표현
description : Dynamic Programming
"""

from collections import defaultdict


def solution(N, number):
    total = set()
    dic = defaultdict(set)
    total.add(N)
    dic[1].add(N)

    for i in range(2, 9):
        dic[i].add(int(str(N) * i))
        total.add(int(str(N) * i))

        for j in range(1, i):
            for x in dic[j]:
                for y in dic[i-j]:
                    for value in (x * y, x + y, x - y):
                        dic[i].add(value)
                        total.add(value)

                    if y != 0:
                        dic[i].add(x // y)
                        total.add(x // y)

        if number in total:
            return i
    return -1


if __name__ == '__main__':
    N = 5
    number = 12

    result = solution(N, number)
    print(result)
