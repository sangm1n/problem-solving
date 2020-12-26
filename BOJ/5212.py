"""
푸르고 아름다운 남해에는 많은 섬이 장관을 이루고 있다. 그림이 아니면 볼 수 없을 것 같은 아름다운 장관을 실제로 볼 수 있는 다도해로 상근이는 여행을 떠났다.

다도해에 도착한 상근이는 서울에서 보던 것과는 다른 풍경에 큰 충격을 받았다. 지구 온난화로 인해 해수면이 상승해 섬의 일부가 바다에 잠겨버렸다.

서울로 다시 돌아온 상근이는 이렇게 지구 온난화가 계속 될 경우 남해의 지도는 어떻게 바뀔지 궁금해졌다.

다도해의 지도는 R*C 크기의 그리드로 나타낼 수 있다. 'X'는 땅을 나타내고, '.'는 바다를 나타낸다.

50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다는 사실을 알았다.

상근이는 50년 후 지도를 그려보기로 했다. 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다.
지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다. 50년이 지난 후에도 섬은 적어도 한 개 있다.
또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.
"""

R, C = map(int, input().split())
islands = [list(input()) for _ in range(R)]


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > R-1 or ny > C-1:
            count += 1
            continue

        if islands[nx][ny] == '.':
            count += 1

    if count >= 3:
        islands[x][y] = '#'


for i in range(R):
    for j in range(C):
        if islands[i][j] == 'X':
            dfs(i, j)

pos = []
for i in range(R):
    for j in range(C):
        if islands[i][j] == '#':
            islands[i][j] = '.'

        if islands[i][j] == 'X':
            pos.append((i, j))

pos.sort(key=lambda x: x[1])
x0, x1 = pos[0][1], pos[-1][1]
pos.sort(key=lambda x: x[0])
y0, y1 = pos[0][0], pos[-1][0]

for i in range(y0, y1+1):
    for j in range(x0, x1+1):
        print(islands[i][j], end='')
    print()
