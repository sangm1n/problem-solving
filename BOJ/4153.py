"""
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
"""

import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if sum(arr) == 0:
        break

    arr.sort()
    squared = [x**2 for x in arr]

    print("right" if squared[-1] == (squared[0] + squared[1]) else "wrong")
