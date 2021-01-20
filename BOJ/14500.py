"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 테트로미노
description : Brute Force
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(M):
        # ㅁㅁㅁㅁ
        if i < N and j+3 < M:
            result.append(sum(graph[i][j:j+4]))
        if i+3 < N and j < M:
            result.append(graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j])

        # ㅁㅁ
        # ㅁㅁ
        if i+1 < N and j+1 < M:
            result.append(sum(graph[i][j:j+2]) + sum(graph[i+1][j:j+2]))

        # ㅁ
        # ㅁ
        # ㅁㅁ
        if i+2 < N and j+1 < M:
            result.append(graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1])
            result.append(graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j] + graph[i+2][j+1])
            result.append(graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+2][j])
            result.append(graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1])

        # ㅁ
        # ㅁㅁ
        #   ㅁ
            result.append(graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1])
            result.append(graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j])

        # ㅁ
        # ㅁㅁ
        # ㅁ
            result.append(graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j])
            result.append(graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1])

        # ㅁㅁㅁ
        # ㅁ
        if i+1 < N and j+2 < M:
            result.append(graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j])
            result.append(graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2])
            result.append(graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2])
            result.append(graph[i][j+2] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2])

        #   ㅁㅁ
        # ㅁㅁ
            result.append(graph[i][j+1] + graph[i][j+2] + graph[i+1][j] + graph[i+1][j+1])
            result.append(graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2])

        #   ㅁ
        # ㅁㅁㅁ
            result.append(graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2])
            result.append(graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+1])

print(max(result))
