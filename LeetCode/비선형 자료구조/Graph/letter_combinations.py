"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Letter Combinations of a Phone Number
description : Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in phone[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []

    phone = {
        '1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
        '0': "",
    }
    result = []
    dfs(0, "")

    return result


if __name__ == '__main__':
    digits = "23"
    print(letterCombinations(digits))
