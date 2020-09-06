"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Array Partition 1
description : Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
"""
from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]

    print(arrayPairSum(nums))
