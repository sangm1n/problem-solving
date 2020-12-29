"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 아이들은 사탕을 좋아해
description : 수학
"""

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))

    result = 0
    for c in candy:
        result += c // K

    print(result)
