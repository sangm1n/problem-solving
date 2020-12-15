"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 바닥 공사
description : 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 2 X 3 크기의 바닥을 채우는 경우의 수는 5가지이다.
"""

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
dp[1], dp[2] = 1, 3
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[N])
