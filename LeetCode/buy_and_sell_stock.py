"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Best Time to Buy and Sell Stock
description : Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction, design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""
from typing import List
import sys


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = sys.maxsize
    profit = 0

    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profit = max(profit, prices[i] - min_price)

    return profit


if __name__ == '__main__':
    ex1 = [7, 1, 5, 3, 6, 4]
    ex2 = [7, 6, 4, 3, 1]

    print(maxProfit(ex1))
    print(maxProfit(ex2))
