"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 완주하지 못한 선수
description : Hash
"""

from collections import defaultdict


def solution(participant, completion):
    dic = defaultdict(int)
    for name in participant:
        dic[name] += 1

    for name in completion:
        dic[name] -= 1

    return [key for key, value in dic.items() if value == 1][0]


if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    result = solution(participant, completion)
    print(result)
