"""

"""

N = int(input())
students = []

for i in range(N):
    name, korea, english, math = list(map(str, input().split()))
    students.append((name, int(korea), int(english), int(math)))

result = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

[print(result[i][0]) for i in range(N)]