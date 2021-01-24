"""
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
"""

arr = [2, 4, 6, 8, 10]
print(arr)

def find(number, arr):
    if number in arr:
        print('{} => True'.format(number))
    else:
        print('{} => False'.format(number))

find(5, arr)
find(10, arr)