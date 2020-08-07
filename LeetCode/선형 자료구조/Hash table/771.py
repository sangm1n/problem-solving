"""
Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
from collections import Counter


def numJewelsInStones(J: str, S: str) -> int:
    counter = Counter(S)
    count = 0

    for char in J:
        count += counter[char]

    return count


J = 'aA'
S = 'aAAbbbb'

print(numJewelsInStones(J, S))

"""
Pythonic Way

def numJewelsInStones(J: str, S: str) -> int:
    return sum(s in J for s in S)
"""