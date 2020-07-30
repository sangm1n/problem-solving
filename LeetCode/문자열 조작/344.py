"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""
from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]
    # s.reverse()


a = ['h', 'e', 'l', 'l', 'o']
b = ['H', 'a', 'n', 'n', 'a', 'h']

reverseString(a)
reverseString(b)

print(a, b, sep='\n')
