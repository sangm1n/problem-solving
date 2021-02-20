"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 개똥벌레
description : Prefix Sum
"""

N, H = map(int, input().split())
cave = [int(input()) for _ in range(N)]

up = [0] * (H+2)
down = [0] * (H+2)
result = [0] * (H+2)

for i in range(N):
    height = cave[i]
    if i % 2 == 0:
        down[height+1] += 1
    else:
        up[H - height] += 1

for i in range(2, H+1):
    down[i] += down[i-1]

for i in range(H, -1, -1):
    up[i] += up[i+1]

for i in range(1, H+1):
    result[i] = up[i] + down[i]

print(N-max(result), result.count(max(result)))
