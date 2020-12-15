"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Binary search (by Recursive)
"""


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


N, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N-1)
if result == None:
    print("No data")
else:
    print(result + 1)
