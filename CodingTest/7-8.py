"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 떡볶이 떡 만들기
description : 오늘은 떡볶이 떡을 만드는 날이다. 떡볶이 떡의 길이가 일정하지 않지만 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라 맞춘다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def binary(arr, target, start, end):
    result = 0
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for num in arr:
            if num >= mid:
                count += (num - mid)

        if count < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


N, M = map(int, input().split())
rice = list(map(int, input().split()))

print(binary(rice, M, 0, max(rice)))
