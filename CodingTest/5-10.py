"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 음료수 얼려 먹기
description : N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
"""

N, M = map(int, input().split())
ice = []
for i in range(N):
    ice.append(list(input()))


def check_ice(i, j):
    if i <= -1 or i >= N or j <= -1 or j >= M:
        return False

    if ice[i][j] == '0':
        ice[i][j] = '1'
        check_ice(i+1, j)
        check_ice(i-1, j)
        check_ice(i, j+1)
        check_ice(i, j-1)
        return True
    return False


count = 0
for i in range(N):
    for j in range(M):
        if check_ice(i, j):
            count += 1

print(count)
