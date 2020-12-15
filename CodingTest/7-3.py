"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Binary search (by Loop)
"""


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N-1)
if result == None:
    print('No data')
else:
    print(result)
