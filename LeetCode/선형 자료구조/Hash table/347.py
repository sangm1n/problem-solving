"""
Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.
"""
from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums).most_common(k)
    return [count[i][0] for i in range(len(count))]

    # return list(zip(*Counter(nums).most_common(k)))[0]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))