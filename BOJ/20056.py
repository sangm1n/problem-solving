"""

"""

from collections import deque

N, M, K = map(int, input().split())
graph = [[deque() for _ in range(N)] for _ in range(N)]
ball = deque()
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])
    ball.append([r-1, c-1])


def ball_move():
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    tmp = []
    for _ in range(len(ball)):
        x, y = ball.popleft()

        for _ in range(len(graph[x][y])):
            m, s, d = graph[x][y].popleft()

            nx = ((x + dx[d] * s) + (N * 10000)) % N
            ny = ((y + dy[d] * s) + (N * 10000)) % N
            tmp.append([nx, ny, m, s, d])
            ball.append([nx, ny])

    for nx, ny, m, s, d in tmp:
        graph[nx][ny].append([m, s, d])


def ball_occur():
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                m_sum, s_sum, odd_count, even_count = 0, 0, 0, 0

                len_graph = len(graph[i][j])
                for k in range(len_graph):
                    m, s, d = graph[i][j].popleft()
                    m_sum += m
                    s_sum += s

                    if d % 2 == 0:
                        even_count += 1
                    elif d % 2 == 1:
                        odd_count += 1

                m, s = m_sum // 5, s_sum // len_graph

                if m != 0:
                    if even_count == len_graph or odd_count == len_graph:
                        for k in range(0, 8, 2):
                            graph[i][j].append([m, s, k])
                    else:
                        for k in range(1, 9, 2):
                            graph[i][j].append([m, s, k])


while K > 0:
    ball_move()
    ball_occur()
    K -= 1

result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            for m, s, d in graph[i][j]:
                result += m

print(result)
