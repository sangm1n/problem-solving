"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 구간 합
"""

N = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left, right = 2, 4
print(prefix_sum[right] - prefix_sum[left - 1])
