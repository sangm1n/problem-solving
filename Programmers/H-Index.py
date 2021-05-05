"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : H-Index
description : Sorting
"""


def solution(citations):
    citations.sort()
    total = len(citations)

    for i in range(total):
        if citations[i] >= total - i:
            return total - i
    return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]

    result = solution(citations)
    print(result)
