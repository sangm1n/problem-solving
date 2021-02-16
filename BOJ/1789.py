"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 수들의 합
description : Binary Search
"""

S = int(input())

result = 0
count = 1
while True:
    result += count

    if result > S:
        break
    count += 1

print(count-1)
