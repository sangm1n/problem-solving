"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 카드
description : Sorting
"""

from collections import Counter

N = int(input())
card = [int(input()) for _ in range(N)]

count = Counter(card)
result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])
