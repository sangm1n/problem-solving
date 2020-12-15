"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

string = input().rstrip()
arr = string.split('-')

result = 0
for i in arr[0].split('+'):
    result += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)
