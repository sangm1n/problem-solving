"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Group Anagrams
description : Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_dict = collections.defaultdict(list)
    for word in strs:
        anagram_dict[''.join(sorted(word))].append(word)

    return anagram_dict.values()


if __name__ == '__main__':
    ex1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ex2 = [""]
    ex3 = ["a"]

    print(groupAnagrams(ex1))
    print(groupAnagrams(ex2))
    print(groupAnagrams(ex3))
