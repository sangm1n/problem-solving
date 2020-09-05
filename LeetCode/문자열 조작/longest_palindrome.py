"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Longest Palindrome Substring
description : Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""
def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    max = ''
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                left -= 1
                right += 1
                if s[left] != s[right]:
                    max = s[left + 1:right]
                    break
        elif s[i] == s[i + 2]:
            left, right = i, i + 2
            while left >= 0 and right < len(s):
                left -= 1
                right += 1
                if s[left] != s[right]:
                    max = s[left + 1:right]
                    break

    return max


if __name__ == '__main__':
    ex1 = "babad"
    ex2 = "cbbd"

    print(longestPalindrome(ex1))
    print(longestPalindrome(ex2))

