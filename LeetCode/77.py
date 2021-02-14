"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Combinations
description : combination
"""

from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1, n+1)]
        result = list(combinations(arr, k))

        return result


if __name__ == "__main__":
    n = 4
    k = 2

    solution = Solution()
    print(solution.combine(n, k))
