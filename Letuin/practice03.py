"""
숫자 이미지

bfs가 빠른 이유 : 함수를 호출하지 않아서
함수를 호출하는게 왜 느리지 ?
메모리는 스택, 힙, 데이터, 코드 네 가지 영역이 있는데,
스택 영역에는 1. 로컬 변수 / 2. 파라미터 / 3. 돌아갈 코드 세 가지가 들어가니까
"""

from collections import deque


def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = True


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, visited)
            result += 1

print(result)
