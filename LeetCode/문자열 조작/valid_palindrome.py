"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Valid Palindrome
description : Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
import re


def isPalindrome(s: str) -> bool:
    lower_s = s.lower()
    normal_s = re.sub('[^a-z0-9]', '', lower_s)

    if normal_s == normal_s[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    ex1 = "A man, a plan, a canal: Panama"
    ex2 = "race a car"

    print(isPalindrome(ex1))
    print(isPalindrome(ex2))


"""
return True / return False
이렇게 구분되는 경우 바로 리턴시키기

ex) return normal_s == normal_s[::-1]
"""