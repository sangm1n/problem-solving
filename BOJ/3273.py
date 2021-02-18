"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 두 수의 합
description : Two Pointer
"""

N = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left, right = 0, N-1
result = 0
while left < right:
    if arr[left] + arr[right] > x:
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    else:
        left += 1
        right -= 1
        result += 1

print(result)
