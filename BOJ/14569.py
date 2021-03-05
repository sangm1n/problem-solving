"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 시간표 짜기
description : 비트 연산
"""

N = int(input())
courses = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    courses.append(set(tmp[1:]))

M = int(input())
students = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    students.append(set(tmp[1:]))

for student in students:
    count = 0
    for course in courses:
        if course.intersection(student) == course:
            count += 1
    print(count)
