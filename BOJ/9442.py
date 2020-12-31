"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Sort Me
description :
"""

while True:
    N, string = map(str, input().split())

    if int(N) == 0:
        break

    alpha = [input() for _ in range(int(N))]
    alpha.sort(key=len)

    

    print(alpha)
