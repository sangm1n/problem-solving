"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 시리얼 번호
description : Sorting
"""


def count_total(string):
    result = 0

    for str in string:
        if str.isdigit():
            result += int(str)

    return result


N = int(input())
serial = [input() for _ in range(N)]
answer = sorted(serial, key=lambda x: (len(x), count_total(x), x))
[print(ans) for ans in answer]
