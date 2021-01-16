"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 팰린드롬 만들기
description : Brute Force
"""

string = list(input())

if string == string[::-1]:
    print(len(string))
else:
    idx = 1
    while True:
        if string[idx:] == string[:idx-1:-1]:
            break
        idx += 1
    print(len(string) + idx)
