"""
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다.
우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def recursive(num, x, y):
    global arr
    global minus_count, zero_count, plus_count
    start = arr[y][x]

    if num == 0:
        return

    flag = True
    for i in range(y, y + num):
        if not flag:
            break
        for j in range(x, x + num):
            if arr[i][j] != start:
                recursive(num//3, x, y)
                recursive(num//3, x + num//3, y)
                recursive(num//3, x + 2 * num//3, y)
                recursive(num//3, x, y + num//3)
                recursive(num//3, x + num//3, y + num//3)
                recursive(num//3, x + 2 * num//3, y + num//3)
                recursive(num//3, x, y + 2 * num//3)
                recursive(num//3, x + num//3, y + 2 * num//3)
                recursive(num//3, x + 2 * num//3, y + 2 * num//3)

                flag = False
                break

    if flag:
        if start == -1:
            minus_count += 1
        elif start == 0:
            zero_count += 1
        elif start == 1:
            plus_count += 1


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

minus_count = 0
zero_count = 0
plus_count = 0
recursive(N, 0, 0)

print(minus_count)
print(zero_count)
print(plus_count)
