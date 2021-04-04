"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 3진법 뒤집기
description : Implementation
"""


def solution(n):
    change = []

    while n >= 3:
        rest = n % 3
        change.append(str(rest))
        n //= 3
    change.append(str(n))

    result = 0
    for i in range(len(change)):
        sup = len(change) - i - 1
        result += int(change[i]) * 3 ** sup

    return result


if __name__ == '__main__':
    n = 45

    result = solution(n)
    print(result)
