"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Fibonacci (Bottom-up)
"""

# DP table
d = [0] * 100

d[1], d[2] = 1, 1
N = int(input())

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])
