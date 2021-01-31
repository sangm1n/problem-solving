"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 그룹 단어
description : Implementation
"""

N = int(input())

result = 0
words = [list(input()) for _ in range(N)]

for word in words:
    dic = dict()
    flag = True

    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 1
        elif word[i] in dic and word[i-1] == word[i]:
            dic[word[i]] += 1
        else:
            flag = False

    if flag:
        result += 1

print(result)
