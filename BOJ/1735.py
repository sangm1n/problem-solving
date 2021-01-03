"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 분수 합
description : GCD
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


up1, down1 = map(int, input().split())
up2, down2 = map(int, input().split())

up = up1*down2 + up2*down1
down = down1 * down2

num = gcd(up, down)
print(up // num, down // num)
