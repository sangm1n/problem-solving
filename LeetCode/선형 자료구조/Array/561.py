"""
Array Partition 1

Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
"""
from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[::2])


a = [1, 2, 3, 2]
print(arrayPairSum(a))