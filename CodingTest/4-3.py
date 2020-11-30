"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 왕실의 나이트
description : 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
    - 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    - 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이처럼 좌표 평면상 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 구하시오.
이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로, 열 위치를 표현할 때는 a부터 h로 표현한다.
"""

pos = input()
alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8
}

x, y = alphabet[pos[0]], int(pos[1])
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)
