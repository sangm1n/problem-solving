R, C = map(int, input().split())

maps = [list(map(str, input())) for _ in range(R)]


def dfs(arr, x, y):
    global count
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > R-1 or ny > C-1:
            count += 1
            continue

        if arr[nx][ny] == 'X':
            continue

        if arr[nx][ny] == '.':
            count += 1


for i in range(len(maps)):
    for j in range(len(maps[0])):
        count = 0
        if maps[i][j] == 'X':
            dfs(maps, i, j)
            if count == 3 or count == 4:
                maps[i][j] = '$'

idx = []
for i in range(len(maps)):
    tmp = []
    for j in range(len(maps[0])):
        if maps[i][j] == 'X':
            tmp.append(j)
        if maps[i][j] == '$':
            maps[i][j] = '.'
    idx.append(tmp)

row_s, row_e = 0, 0
col_s, col_e = 1e9, 0

for i in range(len(idx)):
    if idx[i]:
        col_s = min(min(idx[i]), col_s)
        col_e = max(max(idx[i]), col_e)

for i in range(len(idx)):
    if not idx[i]:
        continue
    for j in range(col_s, col_e+1):
        print(maps[i][j], end='')
    print()
