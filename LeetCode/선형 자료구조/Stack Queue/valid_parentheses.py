"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Valid Parentheses
description : Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
"""
def isValid(s: str) -> bool:
    stack = []
    table = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return not stack


if __name__ == '__main__':
    ex1 = "()"
    ex2 = "()[]{}"
    ex3 = "(]"

    print(isValid(ex1))
    print(isValid(ex2))
    print(isValid(ex3))
