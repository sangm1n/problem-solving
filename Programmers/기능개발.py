"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 기능개발
description : Implementation
"""


def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            remain //= speeds[i]
        else:
            remain = (remain // speeds[i]) + 1

        days.append(remain)

    start = days[0]
    result = []
    count = 1
    for i in range(1, len(days)):
        if days[i] > start:
            result.append(count)
            start = days[i]
            count = 1
        else:
            count += 1

    result.append(count)
    return result


if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]

    result = solution(progresses, speeds)
    print(result)
