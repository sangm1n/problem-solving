"""
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다.
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다.
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며,
이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다

N × N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline


def quad_tree(n, x, y):
    global image, result

    first = image[y][x]

    flag = True
    for i in range(y, y + n):
        if not flag:
            break

        for j in range(x, x + n):
            if image[i][j] != first:
                result.append('(')
                quad_tree(n//2, x, y)
                quad_tree(n//2, x + n//2, y)
                quad_tree(n//2, x, y + n//2)
                quad_tree(n//2, x + n//2, y + n//2)
                result.append(')')
                flag = False
                break

    if flag:
        result.append(str(first))


N = int(input())
image = [list(map(int, input().rstrip())) for _ in range(N)]

result = []
quad_tree(N, 0, 0)

print(''.join(result))
