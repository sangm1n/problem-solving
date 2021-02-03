"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 타일링
description : Dynamic Programming
"""

while True:
    try:
        N = int(input())

        dp = [1, 1, 3]

        for i in range(3, N+1):
            dp.append(dp[i-1] + 2 * dp[i-2])
        print(dp[N])
    except:
        break
