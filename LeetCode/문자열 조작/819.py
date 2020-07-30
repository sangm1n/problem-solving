"""
Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive. The answer is in lowercase.
"""
import re
from typing import List
from collections import Counter


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub('[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]
    answer = Counter(words).most_common(1)[0][0]

    return answer


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["a"]
print(mostCommonWord(paragraph, banned))