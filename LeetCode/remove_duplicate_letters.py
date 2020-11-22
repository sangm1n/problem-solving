"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Remove Duplicate Letters
description : Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
"""
import collections


def removeDuplicateLetters(s: str) -> str:
    counter = collections.Counter(s)
    stack, store = [], set()

    for char in s:
        counter[char] -= 1
        if char in store:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            store.remove(stack.pop())

        stack.append(char)
        store.add(char)

    return ''.join(stack)


if __name__ == '__main__':
    ex1 = "bcabc"
    ex2 = "cbacdcbc"

    print(removeDuplicateLetters(ex1))
    print(removeDuplicateLetters(ex2))
