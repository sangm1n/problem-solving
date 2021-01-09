"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 쇠막대기
description : Dictionary
"""

bar = input()
stack = []

result = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')
    elif bar[i] == ')':
        stack.pop()
        if bar[i-1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)
