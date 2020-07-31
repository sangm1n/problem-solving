"""
Longest Palindrome Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    answer = ''
    for i in range(len(s)):
        answer = max(answer, expand(i, i+1), expand(i, i+2), key=len)

    return answer


a = 'babad'
b = 'ccd'

print(longestPalindrome(a))
print(longestPalindrome(b))