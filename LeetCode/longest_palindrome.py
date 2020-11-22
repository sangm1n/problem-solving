"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Longest Palindrome Substring
description : Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""
def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) == 1 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


if __name__ == '__main__':
    ex1 = "babad"
    ex2 = "cbbd"

    print(longestPalindrome(ex1))
    print(longestPalindrome(ex2))

