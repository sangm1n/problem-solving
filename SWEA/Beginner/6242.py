"""
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
"""

blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = ab = b = o = 0

for i in blood:
    if i == 'A': a += 1
    elif i == 'B': b += 1
    elif i == 'AB': ab += 1
    else: o += 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (a, o, b, ab))

