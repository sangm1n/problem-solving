"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 정렬된 배열에서 특정 수의 개수 구하기
description : Binary Search
"""

import bisect

N, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect.bisect_left(arr, x)
right = bisect.bisect_right(arr, x)

if right - left == 0:
    print(-1)
else:
    print(right - left)
