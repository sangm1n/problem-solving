"""
8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다.
알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다.
열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다.
예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

킹은 다음과 같이 움직일 수 있다.

- R : 한 칸 오른쪽으로
- L : 한 칸 왼쪽으로
- B : 한 칸 아래로
- T : 한 칸 위로
- RT : 오른쪽 위 대각선으로
- LT : 왼쪽 위 대각선으로
- RB : 오른쪽 아래 대각선으로
- LB : 왼쪽 아래 대각선으로

체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.

입력으로 킹이 어떻게 움직여야 하는지 주어진다.
입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.
"""

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, -1, 1, 1]

move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, N = map(str, input().split())

k_pos = [alpha.index(king[0]), 8 - int(king[1])]
s_pos = [alpha.index(stone[0]), 8 - int(stone[1])]

for _ in range(int(N)):
    idx = move.index(input())

    nx = k_pos[0] + dx[idx]
    ny = k_pos[1] + dy[idx]

    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue

    if nx == s_pos[0] and ny == s_pos[1]:
        px = s_pos[0] + dx[idx]
        py = s_pos[1] + dy[idx]

        if px < 0 or py < 0 or px > 7 or py > 7:
            continue

        s_pos[0] = px
        s_pos[1] = py

    k_pos[0] = nx
    k_pos[1] = ny

k_result = alpha[k_pos[0]] + str(8 - k_pos[1])
s_result = alpha[s_pos[0]] + str(8 - s_pos[1])

print(k_result)
print(s_result)
