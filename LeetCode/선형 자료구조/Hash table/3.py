"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
"""


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0

    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char]+1
        else:
            max_length = max(max_length, i-start+1)

        used[char] = i

    return max_length


a = 'abcabcbb'
b = 'bbbbb'
c = 'pwwkew'

print(lengthOfLongestSubstring(a))
print(lengthOfLongestSubstring(b))
print(lengthOfLongestSubstring(c))


"""
double-for loop 이용

def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0

    for i, char in enumerate(s):
        mapping = dict()
        for j in range(i, len(s)):
            if s[j] in mapping:
                break
            mapping[s[j]] = j
            max_length = max(max_length, len(mapping))

    return max_length
"""