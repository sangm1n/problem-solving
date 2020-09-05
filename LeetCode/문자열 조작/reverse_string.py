"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Reverse String
description : Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


def reverseString(s: List[str]) -> None:
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1


if __name__ == '__main__':
    ex1 = ['h', 'e', 'l', 'l', 'o']
    ex2 = ['H', 'a', 'n', 'n', 'a', 'h']

    reverseString(ex1)
    reverseString(ex2)
    print(ex1)
    print(ex2)
