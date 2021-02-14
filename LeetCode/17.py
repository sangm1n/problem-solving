"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Letter Combinations of a Phone Number
description : Combination
"""

from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
                  ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
                  ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        if not digits:
            return []

        digit = list(map(int, digits))
        select = []
        for d in digit:
            select.append(number[d])

        prod = list(product(*select))
        result = []
        for char in prod:
            tmp = ""
            for c in char:
                tmp += c
            result.append(tmp)

        return result


if __name__ == "__main__":
    digits = "23"

    solution = Solution()
    print(solution.letterCombinations(digits))
