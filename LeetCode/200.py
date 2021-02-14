"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Number of Islands
description : DFS
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(visited, i, j):
            stack = []
            stack.append((i, j))
            visited[i][j] = True

            while stack:
                x, y = stack.pop()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1' and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(visited, i, j)
                    result += 1

        return result


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    solution = Solution()
    print(solution.numIslands(grid))
