"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Permutations
description : Given a collection of distinct integers, return all possible permutations.
"""
from typing import List
import itertools


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(nums))
