"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 금광
description : Dynamic Programming
"""

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))

    gold = []
    idx = 0
    for _ in range(N):
        gold.append(tmp[idx:idx+M])
        idx += M

    for j in range(1, M):
        for i in range(N):
            if i == 0:
                gold[i][j] = max(gold[i][j-1] + gold[i][j], gold[i+1][j-1] + gold[i][j])
            elif i == N-1:
                gold[i][j] = max(gold[i-1][j-1] + gold[i][j], gold[i][j-1] + gold[i][j])
            else:
                gold[i][j] = max(gold[i-1][j-1] + gold[i][j], gold[i][j-1] + gold[i][j], gold[i+1][j-1] + gold[i][j])

    result = 0
    for g in gold:
        result = max(result, max(g))
    print(result)
