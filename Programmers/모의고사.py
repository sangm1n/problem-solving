"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 모의고사
description : Math
"""


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    arr = [0, 0, 0]
    for idx, value in enumerate(answers):
        if value == one[idx % len(one)]:
            arr[0] += 1
        if value == two[idx % len(two)]:
            arr[1] += 1
        if value == three[idx % len(three)]:
            arr[2] += 1

    max_value = max(arr)

    result = []
    for idx, value in enumerate(arr):
        if value == max_value:
            result.append(idx + 1)

    return result


if __name__ == '__main__':
    answers = [1, 3, 2, 4, 2]

    result = solution(answers)
    print(result)
