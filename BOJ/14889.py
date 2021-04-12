"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 스타트와 링크
description : Brute Force
"""

from itertools import combinations


def calculate(arr, S):
    total = 0
    for i in arr:
        for j in arr:
            if i != j:
                total += S[i][j]

    return total


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

num = [x for x in range(N)]
compare = set()

result = int(1e9)
for team in list(combinations(num, N // 2)):
    start = team
    link = tuple(set(num) - set(team))

    if start in compare or link in compare:
        break

    compare.add(start)
    compare.add(link)

    start_sum = calculate(start, S)
    link_sum = calculate(link, S)

    diff = abs(start_sum - link_sum)
    result = min(result, diff)

print(result)
