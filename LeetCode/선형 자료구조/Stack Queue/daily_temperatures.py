"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Daily Temperatures
description : Given a list of daily temperatures T, return a list such that,
for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""
from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:
    count = [0] * len(T)
    stack = []

    for i in range(len(T)):
        while stack and T[stack[-1]] < T[i]:
            last = stack.pop()
            count[last] = i - last

        stack.append(i)

    return count


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    print(dailyTemperatures(T))
