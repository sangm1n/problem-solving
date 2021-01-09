"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 베스트셀러
description : Dictionary
"""

from collections import Counter

N = int(input())
book = [input() for _ in range(N)]
book.sort()

count = Counter(book)
print(count.most_common(1)[0][0])
