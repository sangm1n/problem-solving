"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 타일 장식물
description : Dynamic Programming
"""

N = int(input())

arr = [0, 1, 1]
for i in range(3, 81):
    arr.append(arr[i-1] + arr[i-2])

if N == 1:
    print(4)
else:
    w, h = arr[N] + arr[N-1], arr[N]
    print(2 * (w + h))
