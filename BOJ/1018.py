"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 체스판 다시 칠하기
description : Brute Force
"""

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

black, white = list('BWBWBWBW'), list('WBWBWBWB')
black_start, white_start = [], []
for _ in range(4):
    black_start.append(black)
    black_start.append(white)
    white_start.append(white)
    white_start.append(black)

black_cnt, white_cnt = int(1e9), int(1e9)
for i in range(N-7):
    for j in range(M-7):
        black_tmp, white_tmp = 0, 0
        for x in range(8):
            for y in range(8):
                if board[x+i][y+j] != black_start[x][y]:
                    black_tmp += 1
                if board[x+i][y+j] != white_start[x][y]:
                    white_tmp += 1
        black_cnt = min(black_cnt, black_tmp)
        white_cnt = min(white_cnt, white_tmp)

print(min(black_cnt, white_cnt))
