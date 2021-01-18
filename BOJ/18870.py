"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 좌표 압축
description : Sorting
"""

import sys
input = sys.stdin.readline

N = int(input())
coord = list(map(int, input().split()))

trans = list(sorted(set(coord)))
dic = {value: idx for idx, value in enumerate(trans)}

for c in coord:
    print(dic[c], end=' ')
