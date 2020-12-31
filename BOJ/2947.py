"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 나무 조각
description : Implementation
"""

arr = list(map(int, input().split()))

while True:
    if arr == [1, 2, 3, 4, 5]:
        break

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
