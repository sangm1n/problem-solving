"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 국영수
description : Sorting
"""

N = int(input())
score = [list(map(str, input().split())) for _ in range(N)]

score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
[print(x[0]) for x in score]
