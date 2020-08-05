"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""


def isValid(s: str) -> bool:
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


a = "(){}[]"
b = "{()}"
c = "([)]"

print(isValid(a))
print(isValid(b))
print(isValid(c))
