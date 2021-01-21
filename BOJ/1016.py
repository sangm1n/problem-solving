"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 제곱ㄴㄴ수
description : 에라토스테네스의 체
"""

a, b = map(int, input().split())
total = b - a + 1
check = [False] * (total + 1)

count = 0
idx = 2
while True:
    val = idx ** 2
    start = a // val

    if val > b:
        break

    if a % val != 0:
        start += 1

    while start * val <= b:
        if not check[start * val - a]:
            check[start * val - a] = True
            count += 1
        start += 1
    idx += 1

print(total - count)
