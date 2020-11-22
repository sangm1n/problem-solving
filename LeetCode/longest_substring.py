"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Longest Substring Without Repeating Characters
description : Given a string s, find the length of the longest substring without repeating characters.
"""
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0

    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, i-start+1)

        used[char] = i

    return max_length


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))
    print(lengthOfLongestSubstring(s3))
