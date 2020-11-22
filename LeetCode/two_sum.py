"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Two Sum
description : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target-num]]


if __name__ == '__main__':
    ex1 = [2, 7, 11, 15]
    target1 = 9
    ex2 = [3, 2, 4]
    target2 = 6
    ex3 = [3, 3]
    target3 = 6

    print(twoSum(ex1, target1))
    print(twoSum(ex2, target2))
    print(twoSum(ex3, target3))
