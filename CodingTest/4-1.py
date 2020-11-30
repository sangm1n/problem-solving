"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 상하좌우
description : 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 잇으며, 시작 좌표는 항상 (1, 1)이다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
    - L : 왼쪽으로 한 칸 이동
    - R : 오른쪽으로 한 칸 이동
    - U : 위로 한 칸 이동
    - D : 아래로 한 칸 이동
이때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
"""

N = int(input())
direction = list(map(str, input().split()))
x, y = (1, 1)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for direct in direction:
    idx = move.index(direct)

    nx = x + dx[idx]
    ny = y + dy[idx]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny

print(x, y)

