"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 좌표 정렬하기
description : Sorting
"""

N = int(input())
coord = []
for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort(key=lambda x: (x[0], x[1]))

for x, y in coord:
    print(x, y)
