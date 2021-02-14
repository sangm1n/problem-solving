"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Subsets
description : Combination
"""

from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            comb = list(combinations(nums, i))
            for c in comb:
                result.append(c)

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    print(solution.subsets(nums))
