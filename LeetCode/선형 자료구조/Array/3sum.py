"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 3Sum
description : Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0 ?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

    return result


if __name__ == '__main__':
    ex1 = [-1, 0, 1, 2, -1, -4]
    ex2 = []
    ex3 = [0]

    print(threeSum(ex1))
    print(threeSum(ex2))
    print(threeSum(ex3))
