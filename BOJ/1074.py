"""
한수는 크기가 2^N × 2^N인 2차원 배열을 Z모양으로 탐색하려고 한다.
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2^(N-1) × 2^(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def recursive(size, x, y):
    global count
    if x == r and y == c:
        print(count)
        return

    if size == 1:
        count += 1
        return

    if not (x <= r < x + size and y <= c < y + size):
        count += size * size
        return

    recursive(size//2, x, y)
    recursive(size//2, x, y + size//2)
    recursive(size//2, x + size//2, y)
    recursive(size//2, x + size//2, y + size//2)


N, r, c = map(int, input().split())

count = 0
recursive(2**N, 0, 0)
