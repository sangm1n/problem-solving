"""
Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
"""
from collections import Counter


def removeDuplicateLetters(s: str) -> str:
    counter = Counter(s)
    stack, temp = [], set()

    for char in s:
        counter[char] -= 1

        if char in stack:
            continue

        while stack and counter[stack[-1]] > 0 and char < stack[-1]:
            temp.remove(stack.pop())
        stack.append(char)
        temp.add(char)

    return ''.join(stack)


a = "bcabc"
b = "cbacdcbc"

print(removeDuplicateLetters(a))
print(removeDuplicateLetters(b))