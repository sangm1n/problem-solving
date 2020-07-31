"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = dict()

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target-num]]


nums = [3, 0, 4, 3]
target = 6

print(twoSum(nums, target))
