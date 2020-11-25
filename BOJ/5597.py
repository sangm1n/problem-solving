"""
X대학 M교수님은 프로그래밍 수업을 맡고 있습니다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있습니다.
교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하세요.
"""

students = [x for x in range(1, 31)]
result = []

for i in range(28):
    N = int(input())
    if N in students:
        students[students.index(N)] = -1

for student in students:
    if student != -1:
        result.append(student)

print(result[0], result[1], end='\n')