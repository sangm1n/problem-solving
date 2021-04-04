"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 체육복
description : Greedy Algorithm
"""


def solution(n, lost, reserve):
    students = [1] * (n + 1)
    students[0] = -1

    for i in lost:
        students[i] -= 1

    for i in reserve:
        students[i] += 1

    for i in range(1, len(students)):
        if students[i] == 2:
            if students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
                continue
            if i + 1 < len(students) and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1

    answer = [x for x in students if x > 0]
    return len(answer)


if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    result = solution(n, lost, reserve)
    print(result)
