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
    for i in range(0, N*M, M):
        gold.append(list(tmp[i:i+M]))

    base = [[0] * M for _ in range(N)]

    for i in range(N):
        base[i][0] = gold[i][0]

    for j in range(1, M):
        for i in range(N):
            now = gold[i][j]
            if i - 1 < 0:
                base[i][j] = max(base[i][j-1] + now, base[i+1][j-1] + now)
            elif i + 1 > N - 1:
                base[i][j] = max(base[i-1][j-1] + now, base[i][j-1] + now)
            else:
                base[i][j] = max(base[i-1][j-1] + now, base[i][j-1] + now, base[i+1][j-1] + now)

    result = 0
    for i in range(N):
        if base[i][-1] > result:
            result = base[i][-1]

    print(result)
