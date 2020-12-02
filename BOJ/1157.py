"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
"""

from collections import Counter

alphabet = input()
alphabet = alphabet.upper()

alpha_dict = Counter(alphabet)
result = alpha_dict.most_common(2)

if len(result) == 1:
    print(result[0][0])
elif result[0][1] == result[1][1]:
    print('?')
else:
    print(result[0][0])
