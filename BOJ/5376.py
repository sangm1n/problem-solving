"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 소수를 분수로
description : GCD
"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


T = int(input())
for _ in range(T):
    N = list(input().split('('))

    if len(N) == 1:
        up = int(N[0][2:])
        down = 10 ** (len(N[0][2:]))
        num = gcd(up, down)
    else:
        tmp = []
        tmp.append(N[0][2:])
        tmp.append(N[1][:-1])

        base = int(tmp[0] + tmp[1])
        if not tmp[0]:
            up = base
        else:
            up = base - int(tmp[0])
        down = '9' * len(tmp[1]) + '0' * len(tmp[0])
        down = int(down)
        num = gcd(up, down)

    print('{}/{}'.format(up//num, down//num))
