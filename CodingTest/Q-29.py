"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 공유기 설치
description : Parametric Search
"""

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

left = 1
right = house[-1] - house[0]

result = 0
while left <= right:
    mid = (left + right) // 2
    val = house[0]
    count = 1

    for i in range(1, N):
        if mid <= house[i] - val:
            val = house[i]
            count += 1

    if count >= C:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
