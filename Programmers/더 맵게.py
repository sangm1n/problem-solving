"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 더 맵게
description : Heap
"""


import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            return count

        if not scoville:
            return -1

        second = heapq.heappop(scoville)
        new_scoville = first + 2 * second
        heapq.heappush(scoville, new_scoville)

        count += 1


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7

    result = solution(scoville, K)
    print(result)
