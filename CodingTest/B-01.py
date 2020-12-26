"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 소수 판별
"""


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(is_prime_number(4))
print(is_prime_number(7))