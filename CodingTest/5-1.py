"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Stack
"""

stack = []

# 5 삽입 -> 2 삽입 -> 3 삽입 -> 7 삽입 -> 삭제 -> 1 삽입 -> 4 삽입 -> 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
