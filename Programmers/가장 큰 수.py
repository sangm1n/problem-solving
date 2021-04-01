"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 가장 큰 수
description : Sorting
"""


def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: -(int(x[0])))
    result = int("".join(arr))
    print(arr)

    return str(result)


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]

    result = solution(numbers)
    print(result)
