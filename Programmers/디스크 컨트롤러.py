"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 디스크 컨트롤러
description : Heap
"""

import heapq


def solution(jobs):
    hq = []
    idx, result = 0, 0
    start, now = -1, 0

    while idx < len(jobs):
        for request, time in jobs:
            if start < request <= now:
                heapq.heappush(hq, (time, request))

        if hq:
            time, request = heapq.heappop(hq)
            start = now
            now += time
            result += now - request
            idx += 1
        else:
            now += 1

    return result // len(jobs)


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]

    result = solution(jobs)
    print(result)
