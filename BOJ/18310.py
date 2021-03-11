"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 안테나
description : Sorting
"""

N = int(input())
antenna = list(map(int, input().split()))
antenna.sort()
print(antenna[(len(antenna) // 2) - 1])
