"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 프린터
description : Queue
"""

from collections import deque


def check_queue(q, pri):
    for idx, val in q:
        if val > pri:
            return False
    return True


def solution(priorities, location):
    q = deque()
    for idx, val in enumerate(priorities):
        q.append((idx, val))

    count = 1
    while q:
        now, paper = q.popleft()

        if check_queue(q, paper):
            if now == location:
                return count
            count += 1
        else:
            q.append((now, paper))


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2

    result = solution(priorities, location)
    print(result)
