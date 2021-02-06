"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 파일 합치기
description : Dynamic Programming
"""

T = int(input())
for _ in range(T):
    N = int(input())
    books = list(map(int, input().split()))

    dp = [0] * 10001

    for i in range(len(books)):
        for j in range(len(books)):
            if i == j:
                continue

            
