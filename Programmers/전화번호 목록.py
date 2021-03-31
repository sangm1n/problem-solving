"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 전화번호 목록
description : Hash
"""

from collections import defaultdict


def solution(phone_book):
    dic = defaultdict(int)

    for phone in phone_book:
        dic[phone] += 1

    for phone in phone_book:
        tmp = ""
        for num in phone:
            tmp += num
            if dic[tmp] == 1 and tmp != phone:
                return False
    return True


if __name__ == '__main__':
    phone_book = ["123", "456", "789"]

    result = solution(phone_book)
    print(result)
