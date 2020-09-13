"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Top K Frequent Elements
description : Given a non-empty array of integers, return the k most frequent elements.
"""
from typing import List
import collections


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    freq = count.most_common(k)
    result = [freq[x][0] for x in range(len(freq))]

    # return list(zip(*freq))[0]
    return result


if __name__ == '__main__':
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    nums2, k2 = [1], 1

    print(topKFrequent(nums1, k1))
    print(topKFrequent(nums2, k2))

    