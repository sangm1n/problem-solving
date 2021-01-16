"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
description : Brute Force
"""

from collections import defaultdict

N, M = map(int, input().split())
forbid = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    forbid[a].append(b)
    forbid[b].append(a)

count = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j in forbid[i]:
            continue

        for k in range(j+1, N+1):
            if k in forbid[i] or k in forbid[j]:
                continue
            count += 1

print(count)
