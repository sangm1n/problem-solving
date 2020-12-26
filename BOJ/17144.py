"""
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다.
공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다.
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    - 확산되는 양은 Ar,c/5이고 소수점은 버린다.
    - (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
2. 공기청정기가 작동한다.
    - 공기청정기에서는 바람이 나온다.
    - 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
"""

from collections import deque

R, C, T = map(int, input().split())
dust = []
for _ in range(R):
   dust.append(list(map(int, input().split())))


def diffusion():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    zero = [[0] * C for _ in range(R)]
    tmp = dust.copy()

    for i in range(R):
        for j in range(C):
            if dust[i][j] != 0 and dust[i][j] != -1:
                count, diffuse = 0, 0
                for k in range(4):
                    if tmp[i][j] < 5:
                        continue

                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or ny < 0 or nx > R-1 or ny > C-1 or tmp[nx][ny] == -1:
                        continue

                    count += 1
                    diffuse = tmp[i][j] // 5
                    zero[nx][ny] += diffuse
                zero[i][j] += (tmp[i][j] - diffuse * count)

    for i in range(R):
        for j in range(C):
            if dust[i][j] != -1:
                dust[i][j] = zero[i][j]


def get_pos():
    result = []
    for i in range(R):
        for j in range(C):
            if dust[i][j] == -1:
                result.append((i, j))

    return result


def up(x):
    q = deque()

    tmp = dust[x][1:]
    q.append(tmp.pop())
    dust[x][1:] = [0] + tmp

    for i in range(x-1, -1, -1):
        q.append(dust[i].pop())
        dust[i].append(q.popleft())

    q.append(dust[0][0])
    dust[0] = dust[0][1:-1] + [q.popleft(), dust[0][-1]]

    for i in range(1, x):
        q.append(dust[i][0])
        dust[i][0] = q.popleft()


def down(x):
    q = deque()

    tmp = dust[x][1:]
    q.append(tmp.pop())
    dust[x][1:] = [0] + tmp

    for i in range(x+1, R):
        q.append(dust[i].pop())
        dust[i].append(q.popleft())

    q.append(dust[R-1][0])
    dust[R-1] = dust[R-1][1:-1] + [q.popleft(), dust[R-1][-1]]

    for i in range(R-2, x, -1):
        q.append(dust[i][0])
        dust[i][0] = q.popleft()


for _ in range(T):
    diffusion()
    up_pos, down_pos = get_pos()

    up(up_pos[0])
    down(down_pos[0])

result = 0
for i in range(R):
    for j in range(C):
        if dust[i][j] != -1:
            result += dust[i][j]

print(result)
