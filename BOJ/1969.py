"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : DNA
description : Brute Force
"""

from collections import defaultdict

N, M = map(int, input().split())
dna = [input() for _ in range(N)]

result = ""
count = 0
for i in range(len(dna[0])):
    dic = defaultdict(int)
    for j in range(len(dna)):
        dic[dna[j][i]] += 1

    dic_sort = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    hamming = dic_sort[0][0]
    result += hamming

    for j in range(len(dna)):
        if dna[j][i] != hamming:
            count += 1

print(result)
print(count)
