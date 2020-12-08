"""
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

    1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
    2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
"""

import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    result1, result2, result3 = arr[0], arr[0], arr[0]
    result4 = 0
else:
    result1 = round(sum(arr) / N)

    sorted_arr = sorted(arr)
    idx = len(sorted_arr) // 2
    if len(sorted_arr) % 2 == 0:
        result2 = (sorted_arr[idx] + sorted_arr[idx+1]) / 2
    else:
        result2 = sorted_arr[idx]

    count_arr = Counter(arr)
    count_arr = count_arr.most_common()
    sort_arr = sorted(count_arr, key=lambda x: (-x[1], x[0]))
    if sort_arr[0][1] == sort_arr[1][1]:
        result3 = sort_arr[1][0]
    else:
        result3 = sort_arr[0][0]

    result4 = max(arr) - min(arr)

print(result1, result2, result3, result4, sep='\n')
