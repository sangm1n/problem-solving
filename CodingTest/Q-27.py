"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 정렬된 배열에서 특정 수의 개수 구하기
description : Binary Search
"""

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
arr = list(map(int, input().split()))

left, right = bisect_left(arr, x), bisect_right(arr, x)
print(-1 if right - left == 0 else right - left)
