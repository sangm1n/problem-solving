"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : Reorder Data in Log Files
description : You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:
    - Each word after the identifier will consist only of lowercase letters, or;
    - Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.
"""
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    letter, digit = [], []

    for log in logs:
        if log.split()[1].isalpha():
            letter.append(log)
        else:
            digit.append(log)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letter + digit


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    print(reorderLogFiles(logs))
