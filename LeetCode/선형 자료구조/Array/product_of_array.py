"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Product of Array Except Self
description : Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    start = 1
    result = []
    for i in range(len(nums)):
        result.append(start)
        start *= nums[i]

    start = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= start
        start *= nums[i]

    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]

    print(productExceptSelf(nums))
