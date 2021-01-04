"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 괄호
description : Stack
"""

dic = {')': '('}

T = int(input())
for _ in range(T):
    basket = input()
    stack = []

    flag = True
    for b in basket:
        if b == '(':
            stack.append(b)
        elif stack and dic[b] == stack[-1]:
            stack.pop()
        else:
            flag = False

    print("YES" if not stack and flag else "NO")
