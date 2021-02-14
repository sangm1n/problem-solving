"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Permutations
description : Permutation
"""

from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(permutations(nums, len(nums)))

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    print(solution.permute(nums))
