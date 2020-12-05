"""
캥거루 세 마리가 사막에서 놀고 있다. 사막에는 수직선이 하나 있고, 캥거루는 서로 다른 한 좌표 위에 있다.

한 번 움직일 때, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프한다. 한 좌표 위에 있는 캥거루가 두 마리 이상일 수는 없다.

캥거루는 최대 몇 번 움직일 수 있을까?
"""

import sys

while True:
    try:
        kangaroo = list(map(int, sys.stdin.readline().split()))

        count = 0
        flag = [False] * 3
        min_kangaroo = min(kangaroo)
        max_kangaroo = max(kangaroo)

        flag[kangaroo.index(min_kangaroo)] = True
        flag[kangaroo.index(max_kangaroo)] = True
        mid_kangaroo = kangaroo[flag.index(False)]

        if (mid_kangaroo - min_kangaroo) <= (max_kangaroo - mid_kangaroo):
            print(max_kangaroo - mid_kangaroo - 1)
        else:
            print(mid_kangaroo - min_kangaroo - 1)
    except:
        break

