"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Rainbow Beads
description : Sliding Window
"""

N = int(input())
colors = list(input())

result, count = 0, 1
for i in range(1, N):
    if colors[i-1] == 'R' and colors[i] == 'B' or colors[i-1] == 'B' and colors[i] == 'R':
        count += 1
        continue
    result = max(result, count)
    count = 1
result = max(result, count)

print(result)
