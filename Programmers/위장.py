"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 위장
description : Hash
"""

from collections import defaultdict


def solution(clothes):
    dic = defaultdict(list)
    for name, kind in clothes:
        dic[kind].append(name)

    result = 1
    for key, values in dic.items():
        result *= (len(values) + 1)

    return result - 1


if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

    result = solution(clothes)
    print(result)
