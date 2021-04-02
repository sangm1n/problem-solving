"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 타겟 넘버
description : DFS
"""


result = 0


def dfs(numbers, num, idx, target):
    global result

    if idx == len(numbers):
        if num == target:
            result += 1
        return

    dfs(numbers, num + numbers[idx], idx + 1, target)
    dfs(numbers, num - numbers[idx], idx + 1, target)
    return


def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return result


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3

    result = solution(numbers, target)
    print(result)
