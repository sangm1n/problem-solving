"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 문자열 뒤집기
description : 0과 1로만 이루어진 문자열 S가 있다. 이 문자열 S에 있는 모든 숫자를 전부 같게 만드려고 한다.
S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집을 수 있다. (뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.)
예를 들어 S = 0001100일 때는 다음과 같다.
    - 전체를 뒤집으면 1110011이 된다.
    - 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어 두 번만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어 1번 만에 모두 같은 숫자로 만들 수 있다.
문자열 S가 주어졌을 때, 행동의 최소 횟수를 출력하시오.
"""
S = input()

zero_count, one_count = 0, 0

if S[0] == '0':
    one_count += 1
else:
    zero_count += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '0':
            one_count += 1
        else:
            zero_count += 1

print(min(one_count, zero_count))
