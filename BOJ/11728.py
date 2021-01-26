"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 배열 합치기
description : Sorting
"""

N, M = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = first + second
print(*sorted(result))
