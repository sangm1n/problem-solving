"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 이진수 연산
description : 비트 연산
"""

A = int(input(), 2)
B = int(input(), 2)

mask = 2**100000 - 1

print(bin(A & B)[2:].zfill(100000))
print(bin(A | B)[2:].zfill(100000))
print(bin(A ^ B)[2:].zfill(100000))
print(bin(A ^ mask)[2:].zfill(100000))
print(bin(B ^ mask)[2:].zfill(100000))
