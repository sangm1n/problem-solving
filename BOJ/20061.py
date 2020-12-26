"""
모노미노도미노는 아래와 같이 생긴 보드에서 진행되는 게임이다. 보드는 빨간색 보드, 파란색 보드, 초록색 보드가 그림과 같이 붙어있는 형태이다.
게임에서 사용하는 좌표 (x, y)에서 x는 행, y는 열을 의미한다. 빨간색, 파란색, 초록색 보드가 사용하는 좌표는 그 색으로 그림에 적혀있다.

이 게임에서 사용하는 블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태이다. 아래와 같이 세 종류가 있으며, 왼쪽부터 순서대로 크기가 1×1, 1×2, 2×1 이다.

행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리해야 한다.

블록은 보드에 놓인 이후에 다른 블록과 합쳐지지 않는다. 블록을 놓은 위치가 순서대로 주어졌을 때, 얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수를 모두 구해보자.
"""

import sys
input = sys.stdin.readline

N = int(input())

red = [[0] * 4 for _ in range(4)]
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]


def green_domino(t, tile):
    dx, dy = 1, 0

    if t == 1:
        x1, y1 = -1, tile[1]

        while True:
            nx, ny = x1 + dx, y1 + dy

            if nx > 5 or green[nx][ny] != 0:
                break
            x1, y1 = nx, ny

        green[nx-1][ny] = 1
    else:
        if t == 2:
            x1, y1 = -1, tile[0][1]
            x2, y2 = -1, tile[1][1]
        else:
            x1, y1 = -1, tile[0][1]
            x2, y2 = 0, tile[1][1]

        while True:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            if nx1 > 5 or nx2 > 5 or green[nx1][ny1] != 0 or green[nx2][ny2] != 0:
                break

            x1, y1 = nx1, ny1
            x2, y2 = nx2, ny2

        green[nx1-1][ny1] = 1
        green[nx2-1][ny2] = 1


def blue_domino(t, tile):
    dx, dy = 0, 1

    if t == 1:
        x1, y1 = tile[0], -1

        while True:
            nx, ny = x1 + dx, y1 + dy

            if ny > 5 or blue[nx][ny] != 0:
                break
            x1, y1 = nx, ny

        blue[nx][ny-1] = 1
    else:
        if t == 2:
            x1, y1 = tile[0][0], -1
            x2, y2 = tile[1][0], 0
        else:
            x1, y1 = tile[0][0], -1
            x2, y2 = tile[1][0], -1

        while True:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            if ny1 > 5 or ny2 > 5 or blue[nx1][ny1] != 0 or blue[nx2][ny2] != 0:
                break

            x1, y1 = nx1, ny1
            x2, y2 = nx2, ny2

        blue[nx1][ny1-1] = 1
        blue[nx2][ny2-1] = 1


def green_check():
    global score

    for i in range(6):
        if green[i].count(1) == 4:
            for j in range(i, -1, -1):
                green[j] = green[j-1]
            green[0] = [0, 0, 0, 0]
            score += 1

    block_count = 0
    for i in range(2):
        if green[i].count(1) > 0:
            block_count += 1

    for i in range(block_count):
        green.pop()
        green.insert(0, [0, 0, 0, 0])


def blue_check():
    global score

    for i in range(6):
        cnt = 0
        for j in range(4):
            if blue[j][i] == 1:
                cnt += 1

        if cnt == 4:
            for j in range(i, -1, -1):
                for k in range(4):
                    blue[k][j] = blue[k][j-1]
            for j in range(4):
                blue[j][0] = 0
            score += 1

    block_count = 0
    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                block_count += 1
                break

    for i in range(block_count):
        for j in range(4):
            blue[j].pop()
            blue[j].insert(0, 0)


def green_sum():
    global total

    for i in range(6):
        for j in range(4):
            if green[i][j] == 1:
                total += 1


def blue_sum():
    global total

    for i in range(4):
        for j in range(6):
            if blue[i][j] == 1:
                total += 1


score, total = 0, 0
for _ in range(N):
    t, x, y = map(int, input().split())

    if t == 1:
        tile = (x, y)
    elif t == 2:
        tile = [(x, y), (x, y+1)]
    elif t == 3:
        tile = [(x, y), (x+1, y)]

    green_domino(t, tile)
    blue_domino(t, tile)

    green_check()
    blue_check()

green_sum()
blue_sum()

print(score)
print(total)
