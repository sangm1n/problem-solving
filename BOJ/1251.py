"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 단어 나누기
description : Brute Force
"""

from itertools import combinations

word = list(input())
digit = list(range(1, len(word)))

combination = list(combinations(digit, 2))

result = []
for comb in combination:
    one = word[:comb[0]]
    two = word[comb[0]:comb[1]]
    three = word[comb[1]:]

    one = one[::-1]
    two = two[::-1]
    three = three[::-1]
    result.append("".join(one + two + three))

result.sort()
print(result[0])
