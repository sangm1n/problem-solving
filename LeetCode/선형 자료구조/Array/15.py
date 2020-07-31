"""
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    answer = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while left < right:
            num_sum = nums[i] + nums[left] + nums[right]

            if num_sum < 0:
                left += 1
            elif num_sum > 0:
                right -= 1
            elif num_sum == 0:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return answer


a = [-1, 0, 1, 2, -1, -4]
b = [-2, 0, 0, 2, 2]

print(threeSum(a))
print(threeSum(b))
