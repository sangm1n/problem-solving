"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : ROT13
description : Graph
"""

rot = input()

result = ""
for r in rot:
    if r.isalpha() and r.isupper():
        val = chr(ord(r) + 13)
        if ord(val) > 90:
            val = chr(ord(r) - 13)
        result += val
    elif r.isalpha() and r.islower():
        val = chr(ord(r) + 13)
        if ord(val) > 122:
            val = chr(ord(r) - 13)
        result += val
    else:
        result += r

print(result)
