"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Go Latin
description : 문자열
"""

dic = {
    'a': 'as', 'i': 'ios', 'y': 'ios',
    'l': 'les', 'n': 'anes', 'ne': 'anes',
    'o': 'os', 'r': 'res', 't': 'tas',
    'u': 'us', 'v': 'ves', 'w': 'was'
}

T = int(input())
for _ in range(T):
    word = input()

    if word[-1] in dic:
        word = word[:-1] + dic[word[-1]]
    elif word[-2:] in dic:
        word = word[:-2] + dic[word[-2:]]
    else:
        word += 'us'
    print(word)
