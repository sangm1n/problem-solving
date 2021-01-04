"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자의 개수
description : 수학
"""

a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)
arr = [0] * 10

for s in result:
    arr[int(s)] += 1

for i in arr:
    print(i)
