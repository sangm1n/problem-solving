"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : K번째수
description : Sorting
"""


def solution(array, commands):
    result = []
    for start, end, k in commands:
        new_arr = array[start - 1:end]
        new_arr.sort()
        result.append(new_arr[k - 1])

    return result


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    result = solution(array, commands)
    print(result)
