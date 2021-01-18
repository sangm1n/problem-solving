"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 적록색약
description : Hash
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(list)
for _ in range(N):
    site, pwd = map(str, input().split())
    dic[site] = pwd

for _ in range(M):
    print(dic[input().rstrip()])
