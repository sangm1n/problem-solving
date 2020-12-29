"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 괄호 변환
description : Recursive
"""


def correct(p):
    dic = {')': '('}

    stack = []
    for i in p:
        if i not in dic:
            stack.append(i)
        elif stack and dic[i] == stack[-1]:
            stack.pop()

    return len(stack) == 0


def division(p):
    open_count, close_count = 0, 0
    limit = 0
    for idx, val in enumerate(p):
        if val == '(':
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            limit = idx
            break

    return p[:limit + 1], p[limit + 1:]


def solution(p):
    result = ""

    if p == "":
        return result

    u, v = division(p)
    if correct(u):
        result = u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'

        u = list(u[1:-1])
        for idx, val in enumerate(u):
            if val == '(':
                u[idx] = ')'
            else:
                u[idx] = '('
        result += "".join(u)
    return result


p1 = "(()())()"
p2 = ")("
p3 = "()))((()"
print(solution(p1))
print(solution(p2))
print(solution(p3))
