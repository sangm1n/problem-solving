"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 점수 계산
description : Sorting
"""

score = []
for i in range(1, 9):
    val = int(input())
    score.append((val, i))

score.sort(reverse=True)

result = []
total = 0
for i in range(5):
    result.append(score[i][1])
    total += score[i][0]

print(total)
print(*sorted(result))
