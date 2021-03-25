"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 시험 감독
description : 수학
"""

N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())

arr = [0]
max_value = max(people)
for i in range(1, max_value + 1):
    if i - B <= 0:
        arr.append(1)
    else:
        rest = i - B
        if rest - C <= 0:
            arr.append(2)
        elif rest % C == 0:
            arr.append(1 + rest // C)
        else:
            arr.append(1 + rest // C + 1)

result = 0
for p in people:
    result += arr[p]

print(result)
