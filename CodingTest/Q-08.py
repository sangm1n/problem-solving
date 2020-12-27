"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 문자열 재정렬
description : 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 옹름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
"""

S = input()
sum_digit = 0
result = []

for s in S:
    if s.isdigit():
        sum_digit += int(s)
    else:
        result.append(s)

result.sort()
print(''.join(result) + str(sum_digit))
