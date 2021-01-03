"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 종이에 숫자 쓰기
description : 수학
"""

N = float(input())
trans = list(str(N).split('.'))
ten = int(10 ** len(trans[1]))

idx = 0
for i in range(1, ten+1):
    if int(N * i) == float(N * i):
        idx = i
        break

arr = [0, 0, 0, 0, 0]
num = int(N * idx)
for i in range(len(arr), 0, -1):
    if num <= 0:
        break
    arr[i-1] += num // i
    num -= i * (num // i)

print(*arr)
