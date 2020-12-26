"""
어른 상어가 마법사가 되었고, 파이어볼을 배웠다.

마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2. 파이어볼은 4개의 파이어볼로 나누어진다.
    3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    4. 질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
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
