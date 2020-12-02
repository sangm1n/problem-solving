"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로
"""

N = int(input())
alphabet = set()
for i in range(N):
    alphabet.add(input())

alphabet = sorted(alphabet, key=lambda x: (len(x), x[0:]))
for alpha in alphabet:
    print(alpha)
