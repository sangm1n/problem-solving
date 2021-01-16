"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자 정사각형
description : Brute Force
"""

N, M = map(int, input().split())
rect = [list(map(int, str(input()))) for _ in range(N)]

length = 1
result = 0
while length <= N:
    x, y = (0, 0)

    for i in range(N - length):
        for j in range(M - length):
            if rect[i][j] == rect[i][j+length] == rect[i+length][j] == rect[i+length][j+length]:
                result = (length + 1) ** 2

    length += 1

print(result if result != 0 else 1)
