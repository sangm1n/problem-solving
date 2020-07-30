"""
Group Anagrams

Given an array of strings, group anagrams together.
"""
import collections

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


anagram = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams(anagram))
