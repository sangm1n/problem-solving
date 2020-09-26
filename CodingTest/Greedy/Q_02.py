"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 곱하기 혹은 더하기
description : 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽까지 하나씩 모든 숫자를 확인하며
숫자 사이에 '*' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
단, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
"""
S = input()
S = list(map(int, S))

result = S[0]
for i in range(1, len(S)):
    if S[i-1] == 0 or S[i-1] == 1:
        result += S[i]
        continue
    result *= S[i]

print(result)
