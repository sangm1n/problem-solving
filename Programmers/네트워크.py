"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 네트워크
description : DFS
"""


def dfs(v, computers, visited):
    stack = [v]
    visited[v] = True

    while stack:
        i = stack.pop()

        for j in range(len(computers)):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = True
                stack.append(j)


def solution(n, computers):
    visited = [0] * n

    result = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            result += 1

    return result


if __name__ == '__main__':
    n = 3
    network = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    result = solution(n, network)
    print(result)
