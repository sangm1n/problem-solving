"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Jewels and Stones
description : You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
import collections


def numJewelsInStones(J: str, S: str) -> int:
    counter = collections.Counter(J)
    count = 0

    for stone in S:
        count += counter[stone]

    return count


if __name__ == '__main__':
    J1, S1 = "aA", "aAAbbbb"
    J2, S2 = "z", "ZZ"

    print(numJewelsInStones(J1, S1))
    print(numJewelsInStones(J2, S2))
