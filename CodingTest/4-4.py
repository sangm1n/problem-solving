"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 게임 개발
description : 게임 캐릭터가 맵 안에서 움직이는 시스템이 있다.
캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 움직임을 위한 매뉴얼은 다음과 같다.

    - 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
    - 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
    - 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
"""

N, M = map(int, input().split())
A, B, d = map(int, input().split())

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_map[A][B] = '1'
count = 1
dir_count = 0
while True:
    d -= 1
    if d < 0:
        d = 3

    nx = A + dx[d]
    ny = B + dy[d]

    if game_map[nx][ny] == 0:
        game_map[nx][ny] = '1'
        A, B = nx, ny
        count += 1
        dir_count = 0
        continue
    else:
        dir_count += 1

    if dir_count == 4:
        nx = A - dx[d]
        ny = B - dy[d]

        if game_map[nx][ny] == 0:
            A, B = nx, ny
        else:
            break
        dir_count = 0

print(count)
