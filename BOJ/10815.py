"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 숫자 카드
description : Binary Search
"""


def binary_search(target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if card[mid] == target:
            return 1
        elif card[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0


N = int(input())
card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

card.sort()
result = []
for num in check_card:
    result.append(binary_search(num, 0, N-1))

print(*result)
