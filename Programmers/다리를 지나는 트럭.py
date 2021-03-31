"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 다리를 지나는 트럭
description : Hash
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    q = deque()
    q.append([truck_weights.popleft(), 0])

    count = 1
    while True:
        if not q:
            return count

        time = 0
        for i in range(len(q)):
            q[i][1] += 1
            if q[i][1] == bridge_length:
                time += 1

        for _ in range(time):
            q.popleft()

        weight_sum = 0 if not q else sum(list(zip(*q))[0])
        if truck_weights and weight_sum + truck_weights[0] <= weight:
            q.append([truck_weights.popleft(), 0])

        count += 1


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    result = solution(bridge_length, weight, truck_weights)
    print(result)
