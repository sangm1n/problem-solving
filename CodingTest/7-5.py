"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 부품 찾기
description : 전자 매장에는 N개의 부품이 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어는 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
"""

import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    flag = False
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            flag = True
            break

    return flag


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
sub = list(map(int, input().split()))

for num in sub:
    result = binary_search(arr, num, 0, N-1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
