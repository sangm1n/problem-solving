"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
import re


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


a = "A man, a plan, a canal: Panama"
b = "race a car"

print(isPalindrome(a))
print(isPalindrome(b))


"""
# deque 이용

from collections import deque

def isPalindrome(s: str) -> bool:
    dq = deque()
    for char in s:
        if char.isalnum():
            dq.append(char.lower())
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True    
"""