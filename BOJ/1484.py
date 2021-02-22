"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 다이어트
description : Two Pointer
"""

G = int(input())
arr = [int(x**2) for x in range(100001)]

left, right = 1, 2
result = []
while True:
    if right - left == 1 and arr[right] - arr[left] > 100000:
        break

    if arr[right] - arr[left] < G:
        right += 1
    elif arr[right] - arr[left] > G:
        left += 1
    else:
        result.append(right)
        left += 1

if result:
    [print(x) for x in result]
else:
    print(-1)
