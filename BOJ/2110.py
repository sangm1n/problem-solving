"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 공유기 설치
description : Binary Search
"""

N, C = map(int, input().split())
wifi = [int(input()) for _ in range(N)]
wifi.sort()

min_gap, max_gap = 1, wifi[-1] - wifi[0]
result = 0
while min_gap <= max_gap:
    mid_gap = (min_gap + max_gap) // 2

    count = 1
    start = wifi[0]
    for i in range(1, N):
        if mid_gap <= wifi[i] - start:
            count += 1
            start = wifi[i]

    if count >= C:
        result = mid_gap
        min_gap = mid_gap + 1
    else:
        max_gap = mid_gap - 1

print(result)
