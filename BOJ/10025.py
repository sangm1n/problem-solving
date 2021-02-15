"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 게으른 백곰
description : Sliding Window
"""

N, K = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(N)]

arr = [0 for _ in range(1000001)]
for i in range(N):
    arr[zoo[i][1]] = zoo[i][0]

step = K * 2 + 1
tmp = sum(arr[:step])
result = tmp

for i in range(step, 1000001):
    tmp += arr[i] - arr[i-step]
    result = max(result, tmp)

print(result)
