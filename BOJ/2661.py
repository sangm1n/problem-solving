"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 좋은수열
description : Back Tracking
"""

import heapq


def check(string):
    len_str = len(string)

    for size in range(1, (len_str // 2) + 1):
        first = 0
        second = first + size

        for step in range(len_str - 2 * size + 1):
            if string[first + step:first + size + step] == string[second + step:second + size + step]:
                return False
    return True


N = int(input())
arr = ['1', '2', '3']

result = '1'
q = []
heapq.heappush(q, (-1, len(result)))

flag = False
while q:
    length, now = heapq.heappop(q)
    now_string = str(now)

    for num in arr:
        new_string = now_string + num

        if check(new_string):
            if len(new_string) == N:
                print(int(new_string))
                flag = True
                break
            heapq.heappush(q, (-len(new_string), int(new_string)))

    if flag:
        break
