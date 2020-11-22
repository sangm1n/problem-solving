"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Most Common Word
description : Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive. The answer is in lowercase.
"""
import re, collections
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    lower_p = paragraph.lower()
    normal_p = re.sub('[^a-z0-9]', ' ', lower_p)
    list_p = normal_p.split()
    words = [word for word in list_p if word not in banned]

    count = collections.Counter(words)

    return count.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(mostCommonWord(paragraph, banned))
