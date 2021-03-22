"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 입국심사
description : Binary Search
"""

N, M = map(int, input().split())
immigration = [int(input()) for _ in range(N)]

left, right = 0, max(immigration) * M
result = int(1e9)
while left <= right:
    mid = (left + right) // 2

    count = 0
    for wait in immigration:
        count += mid // wait

    if count >= M:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)
